from odoo import models, fields, api, _



class HospitalOpration(models.Model):
   _name = 'hospital.operation'
   _description = 'Hospital Opration'
   _log_access = False

   operation_name = fields.Char(string='Name')
   doctor_id = fields.Many2one(comodel_name='res.users', string='Doctor')
   
   @api.model
   def name_create(self, name):
      return self.create({'operation_name': name}).name_get()[0]