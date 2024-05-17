from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
   _name          = 'hospital.appointment'
   _description   = 'Hospital Appointment'
   _inherit       = ['mail.thread', 'mail.activity.mixin']
   _order         = 'id desc'

   patient_id     = fields.Many2one(comodel_name='hospital.patient', string='Patient', ondelete="set null", tracking=1)
   name           = fields.Char(string='Appointment Name', tracking=2)
   booking_date   = fields.Date(string='Booking Date', default=fields.Date.context_today, tracking=3)
   doctor_id      = fields.Many2one(comodel_name='res.users', string='Dokter', tracking=4)
   gender         = fields.Selection(string='Jenis Kelamin', related='patient_id.gender', tracking=5)
   ref            = fields.Char(string='Reference', help='Referensi untuk kamu', tracking=6)
   
   # name           = fields.Char(string='Appointment Name', tracking=2)
   # patient_id     = fields.Many2one(comodel_name='hospital.patient', string='Patient', ondelete="set null", tracking=1)
   # ref            = fields.Char(string='Reference', help='Referensi untuk kamu', tracking=6)
   # gender         = fields.Selection(string='Jenis Kelamin', related='patient_id.gender', tracking=5)
   # doctor_id      = fields.Many2one(comodel_name='res.users', string='Dokter', tracking=4)
   # booking_date   = fields.Date(string='Booking Date', default=fields.Date.context_today, tracking=3)
   
   appointment_time  = fields.Datetime(string='Appointment Time', default=fields.Datetime.now, tracking=True)
   operation         = fields.Many2one(comodel_name='hospital.operation', string='Operation', tracking=True)
   resep_lines_ids   = fields.One2many(comodel_name='resep.lines', inverse_name='appointment_id', string='Pharmacy Lines', tracking=True)
   hide_sales_price  = fields.Boolean(string='Hide Sales Price', tracking=True)   

   prescription      = fields.Html(string='Prescription')
   priority = fields.Selection([
      ('0', 'Normal'),
      ('1', 'Low'),
      ('2', 'High'),
      ('3', 'Very High'),
   ], string='priority')

   state = fields.Selection([
      ('draft', 'Draft'),
      ('in_consultation', 'In Consultation'),
      ('done', 'Done'),
      ('cancel', 'Cancel'),
   ], string='Status', default="draft", required=True)
   

   @api.onchange('patient_id')
   def _onchange_patient_id(self):
      self.ref = self.patient_id.reference
   
   def action_test(self):
      return {
         'type'   : 'ir.actions.act_url',
         'target' : 'new',
         'url'    : self.name,

      }
   
   def action_state_in_consultation(self) :
      for rec in self : 
         if rec.state == 'draft':
            rec.state = 'in_consultation'

   def unlink(self):
      for rec in self:
         if rec.state == 'done':
            raise ValidationError(_("Tidak bisa hapus status done"))
      return super(HospitalAppointment, self).unlink()

   def action_state_done(self) :
      for rec in self : 
         rec.state = 'done'

   def action_state_cancel(self) :
      action = self.env.ref('om_hospital.cancel_appointment_wizard_action').read()[0]
      return action

   def action_state_draft(self) :
      for rec in self : 
         rec.state = 'draft'

class ResepLines(models.Model):
   _name = 'resep.lines'
   _description = 'Resep'

   product_id = fields.Many2one(comodel_name='product.product', string='Product', required=True)
   qty = fields.Integer(string='Quantity', default="1")
   price_unit = fields.Float(string='Price')
   appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment')
   
   
   
   
