from odoo import models, fields, api

class JabatanWizard(models.TransientModel):
   _name = 'jabatan.wizard'
   _description = 'Jabatan Wizard'

   # def _default_jabatan(self):
   #    return self.env['jabatan'].browse(self._context.get('active_ids'))

   jabatan_id      = fields.Many2one(comodel_name='jabatan', string='Jabatan')
   instruktur_id   = fields.Many2one(comodel_name='instruktur', string='Instruktur')
   instruktur_name = fields.Char(string='Pemangku Jabatan', related='jabatan_id.pejabat.name')
   
   def simpan(self):
      self.jabatan_id.write({'pejabat': self.instruktur_id.id})
      self.instruktur_id.write({'jabatan_id': self.jabatan_id.id})
      
      return {'type': 'ir.actions.act_window_close'}
      # instruktur_record = self.env['instruktur'].search([])
      # for irec in instruktur_record:
      #    irec.jabatan_id = 0

      # jabatan_record = self.env['jabatan'].search([])
      # for jrec in jabatan_record:
      #    jrec.pejabat = 0
         
      # self.jabatan_id.pejabat = self.instruktur_id
      # self.instruktur_id.jabatan_id = self.jabatan_id.id

      
   