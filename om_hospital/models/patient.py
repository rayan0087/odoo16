from odoo import models, fields, api, _
from datetime import date
from odoo.exceptions import ValidationError
from dateutil import relativedelta

class HospitalPatient(models.Model):
   _name          = 'hospital.patient'
   _description   = 'Hospital Patient'
   _inherit       = ['mail.thread', 'mail.activity.mixin']

   name          = fields.Char(string='Nama', tracking=True)
   age           = fields.Integer(string='Umur', compute='_compute_age', 
                                 inverse='_inverse_compute_age', search='_search_age', tracking=True)
   date_of_birth = fields.Date(string='Date of Brith', tracking=True)
   reference     = fields.Char(string='Reference', tracking=True, default='Rayans')
   gender        = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki Laki'), ('p', 'Perempuan')],  tracking=True, default='l')
   image         = fields.Image('Image')
   tag_ids       = fields.Many2many(comodel_name='patient.tag', string='Tags')
   appointment_count = fields.Integer(string='Appointment Count', compute="_compute_appointment_count", store=True)
   appointment_ids = fields.One2many(comodel_name='hospital.appointment', inverse_name='patient_id', string='Appointment')
   

   parent          = fields.Char(string='Parent')
   martial_status  = fields.Selection(string='Martial Status', selection=[('married', 'Married'), ('single', 'Single')], default="single",tracking=True)
   partner_name    = fields.Char(string='Partner Name')
   
   

   active     = fields.Boolean(string='Active', default=True)

   @api.model
   def create(self, vals):
      vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient')
      return super(HospitalPatient, self).create(vals)

   def write(self, vals):
      if not self.reference and not vals.get('reference'):
         vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient')
      return super(HospitalPatient, self).write(vals)

   @api.ondelete(at_uninstall=False)
   def _check_appointments(self):
      for rec in self:
         if rec.appointment_ids:
            raise ValidationError(_("kamu tidak bisa hapus patient dengan appointments"))

   @api.constrains('date_of_birth')
   def _check_date_of_birth(self):
      for rec in self:
         if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
            raise ValidationError(_("Tanggal tidak valid"))

   @api.depends('date_of_birth')
   def _compute_age(self):
      for rec in self:
         today = date.today()
         if rec.date_of_birth:
            rec.age = today.year - rec.date_of_birth.year
         else:
            rec.age = 0

   @api.depends('age')
   def _inverse_compute_age(self):
      today = date.today()
      for rec in self:
         rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)

   def _search_age(self, operator, value):
      date_of_birth = date.today() - relativedelta.relativedelta(years=value)
      start_of_year = date_of_birth.replace(day=1, month=1)
      end_of_year = date_of_birth.replace(day=31, month=12)
      return [('date_of_birth','>=',start_of_year),('date_of_birth','<=',end_of_year)]

   def _compute_appointment_count(self):
      for rec in self:
         rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id','=',rec.id)])
         # rec.appointment_count = 10

   
   @api.onchange('martial_status')
   def _onchange_martial_status(self):
      self.partner_name = ''



   def action_test(self):
      print("clicked")
      return

   def name_get(self):
      # patient_list = []
      # for rec in self:
      #    name = rec.reference + ' - ' +rec.name
      #    patient_list.append(_(rec.id, name))

      return [(rec.id, "[%s]%s" % (rec.reference, rec.name)) for rec in self]




