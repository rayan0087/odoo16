from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Jabatan(models.Model):
   _name        = 'jabatan'
   _description = 'Jabatan'

   name           = fields.Char(string='Nama Jabatan', required=True)
   jenis_jabatan  = fields.Selection([('1', 'Kepala / Pimpinan Lembaga'), ('2', 'Wakil Kepala Lembaga'), ('3', 'Staff ')], default="3", string='Jenis Jabatan', required=True)
   keterangan     = fields.Text('keterangan')
   pejabat        = fields.Many2one(comodel_name='instruktur', string='Daftar Pejabat')
   # instruktur_ids = fields.Many2many('instruktur', string='Instruktur')

   @api.constrains('jenis_jabatan')
   def _check_jabatan_constraints(self):
      for record in self:
         if record.jenis_jabatan == '1':
            existing_kepala = self.search([('jenis_jabatan', '=', '1')])
            if len(existing_kepala) > 1 or (len(existing_kepala) == 1 and existing_kepala.id != record.id):
               raise ValidationError("Hanya boleh ada satu Kepala / Pimpinan Lembaga.")
         elif record.jenis_jabatan == '2':
            existing_wakil = self.search([('jenis_jabatan', '=', '2')])
            if len(existing_wakil) > 1 or (len(existing_wakil) == 1 and existing_wakil.id != record.id):
               raise ValidationError("Hanya boleh ada satu Wakil Kepala Lembaga.")
   
