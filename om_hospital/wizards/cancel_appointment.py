from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date
from dateutil import relativedelta

class CancelAppointmentWizard(models.TransientModel):
   _name = 'cancel.appointment.wizard'
   _description = 'Cancel Apoointment Wizard'

   appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment', 
                                    domain=[('state', '=', 'draft'), ('priority','in',('0','1',False))])
   reason         = fields.Text(string='Reason')
   cancel_date = fields.Date(string='Cancel Date')
   
   @api.model
   def default_get(self, fields):
      res = super(CancelAppointmentWizard, self).default_get(fields)
      res['cancel_date'] = date.today()   
      if self.env.context.get('active_id'):
         res['appointment_id'] = self.env.context.get('active_id')
      return res

   def action_cancel_appointment(self):

      cancel_day = self.env['ir.config_parameter'].get_param('on_hospital.cancel_day')
      allow_date = self.appointment_id.booking_date - relativedelta.relativedelta(days=int(cancel_day))
      if allow_date < date.today():
         raise ValidationError(_("Maaf, anda tidak bisa membatalkan appointment"))

      # if self.appointment_id.booking_date == fields.Date.today():
      #    raise ValidationError(_("Maaf, anda tidak bisa membatalkan appointment dihari yang sama"))
      # self.appointment_id.state = 'cancel'
      # return
   
   
   
   
