from odoo import models, fields, api



class PatientTag(models.Model):
   _name = 'patient.tag'
   _description = 'Patient Tag'

   name = fields.Char(string='Name', required=True)
   active = fields.Boolean(string='active', default=True, copy=False)
   color = fields.Integer(string='Color')
   color_2 = fields.Char(string='Color 2')
   sequence = fields.Integer(string='Sequence')
   
   _sql_constraints = [
      ('unique_tag_name', 'Unique (name, active)', 'Nama sudah ada, harap input nama lain'),
      ('check_sequence', 'Check (sequence > 0)', 'Sequence harus lebih dari 0')
   ]

   @api.returns('self', lambda value:value.id)
   def copy(self, default=None):
      if default is None:
         default = {}

      if not default.get('name'):
         default['name'] = self.name + " (copy)"
      
      default['sequence'] = 10
      return super(PatientTag, self).copy(default)
   
   
