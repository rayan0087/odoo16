from odoo import models, fields, api


class HospitalAppointment(models.Model):
   _name          = 'hospital.appointment'
   _description   = 'Hospital Appointment'
   _inherit       = ['mail.thread', 'mail.activity.mixin']

   name              = fields.Char(string='Appointment Name')
   patient_id        = fields.Many2one(comodel_name='hospital.patient', string='Patient')
   gender            = fields.Selection(string='Jenis Kelamin', related='patient_id.gender')
   appointment_time  = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
   booking_date      = fields.Date(string='Booking Date', default=fields.Date.context_today)
   ref               = fields.Char(string='Reference', help='Referensi untuk kamu')
   doctor_id         = fields.Many2one(comodel_name='res.users', string='Dokter')
   resep_lines_ids   = fields.One2many(comodel_name='resep.lines', inverse_name='appointment_id', string='Pharmacy Lines')
   hide_sales_price = fields.Boolean(string='Hide Sales Price')

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
      print('Button Clicked !!!!!!!')
      return {
         'effect' : {
            'fadeout' : 'slow',
            'message' : 'Suskses Klik',
            'type' : 'rainbow_man',
         }
      }
   
   def action_state_in_consultation(self) :
      for rec in self : 
         rec.state = 'in_consultation'

   def action_state_done(self) :
      for rec in self : 
         rec.state = 'done'

   def action_state_cancel(self) :
      for rec in self : 
         rec.state = 'cancel'

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
   
   
   
   
