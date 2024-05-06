from odoo import models, fields, api
from datetime import date


class HospitalPatient(models.Model):
   _name          = 'hospital.patient'
   _description   = 'Hospital Patient'
   _inherit       = ['mail.thread', 'mail.activity.mixin']

   name          = fields.Char(string='Nama', tracking=True)
   age           = fields.Integer(string='Umur', compute='_compute_age',tracking=True)
   date_of_birth = fields.Date(string='Date of Brith', tracking=True)
   reference     = fields.Char(string='Reference', tracking=True, default='Rayans')
   gender        = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki Laki'), ('p', 'Perempuan')],  tracking=True, default='l')
   
   active     = fields.Boolean(string='Active', default=True)

   @api.depends('date_of_birth')
   def _compute_age(self):
      for rec in self:
         today = date.today()
         if rec.date_of_birth:
            rec.age = today.year - rec.date_of_birth.year
         else:
            rec.age = 0









