from odoo import models, fields, api

class JabatanWizard(models.TransientModel):
   _name = 'jabatan.wizard'
   _description = 'Jabatan Wizard'

   # def _default_jabatan(self):
   #    return self.env['jabatan'].browse(self._context.get('active_ids'))

   jabatan_id  = fields.Many2one(comodel_name='jabatan', string='Jabatan')
   instruktur_ids = fields.Many2many(comodel_name='instruktur', string='Instruktur')

   def tambah_instruktur(self):
      self.jabatan_id.instruktur_ids |= self.instruktur_ids
   