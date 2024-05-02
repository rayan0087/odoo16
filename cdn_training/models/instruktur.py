from odoo import models, fields, api
from odoo.exceptions import ValidationError



class Instruktur(models.Model):
   _name        = 'instruktur'
   _description = 'Instruktur'
   _inherits    = {'res.partner':'partner_id'}

   partner_id        = fields.Many2one(comodel_name='res.partner', string='Partner',required=True,ondelete='cascade')
   keahlian_ids      = fields.Many2many(comodel_name='keahlian', string='Keahlian')
   # jabatan_id        = fields.Many2one(comodel_name='jabatan', string='Jabatan', compute='_compute_jabatan_id', store=True)
   jabatan_id        = fields.Many2one(comodel_name='jabatan', string='Jabatan', default="null")
   jabatan_staf      = fields.Char(string='Jabatan Staf')
   jenis_jabatan     = fields.Selection(string='Jenis Jabatan', related='jabatan_id.jenis_jabatan')
   
   # def action_update_jabatan(self):
   #    self.jabatan_id.pejabat = self.id
   #    return True

   # def _check_jabatan_constraints(self):
   #    related_records = self.env['instruktur'].search([('jabatan_id.jenis_jabatan','=',self.jabatan_id.id)])
   #    for record in related_records:
   #       record.jabatan_id = 0 

class Keahlian(models.Model):
   _name = 'keahlian'
   _description = 'Keahlian'

   name = fields.Char(string='Nama Keahlian', required=True)
   