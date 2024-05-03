from odoo import models, fields, api


class HospitalAppointment(models.Model):
   _name = 'hospital.appointment'
   _description = 'Hospital Appointment'
   _inherit = ['mail.thread', 'mail.activity.mixin']

   name = fields.Char(string='Appointment Name')
   patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient')
   appointment_time = fields.Datetime(string='Appointment Time')
   booking_date = fields.Date(string='Booking Date')
   
   