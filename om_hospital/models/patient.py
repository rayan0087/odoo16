from odoo import models, fields, api


class HospitalPatient(models.Model):
   _name          = 'hospital.patient'
   _description   = 'Hospital Patient'
   _inherit       = ['mail.thread', 'mail.activity.mixin']

   name       = fields.Char(string='Nama', tracking=True)
   age        = fields.Integer(string='Umur', tracking=True)
   reference  = fields.Char(string='Reference', tracking=True)
   gender     = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki Laki'), ('p', 'Perempuan')],  tracking=True)
   
   active     = fields.Boolean(string='Active', default=True)












