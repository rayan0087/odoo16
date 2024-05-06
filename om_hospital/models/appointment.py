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
   ref               = fields.Char(string='Reference')
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
   