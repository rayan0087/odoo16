from odoo import models, fields, api


class HospitalPatient(models.Model):
   _name = 'hospital.patient'
   _description = 'Hospital Patient'

   name = fields.Char(string='Nama')
   age = fields.Integer(string='Umur')
   gender = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki Laki'), ('p', 'Perempuan')])
   
   
   