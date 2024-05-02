from odoo import models, fields, api
from odoo.exceptions import ValidationError



class Instruktur(models.Model):
   _name        = 'instruktur'
   _description = 'Instruktur'
   _inherits    = {'res.partner':'partner_id'}

   partner_id        = fields.Many2one(comodel_name='res.partner', string='Partner',required=True,ondelete='cascade')
   keahlian_ids      = fields.Many2many(comodel_name='keahlian', string='Keahlian')
   # jabatan_id        = fields.Many2one(comodel_name='jabatan', string='Jabatan', compute='_compute_jabatan_id', store=True)
   jabatan_id        = fields.Many2one(comodel_name='jabatan', string='Jabatan')
   jabatan_staf      = fields.Char(string='Jabatan Staf')
   jenis_jabatan     = fields.Selection(string='Jenis Jabatan', related='jabatan_id.jenis_jabatan')
   
   # @api.depends('jabatan_id')
   # def _compute_jabatan_id(self):
   #    # Ambil semua nilai dari field Many2one 'other_model_id'
   #    existing_jabatan_ids = self.env['instruktur'].search([]).mapped('jabatan_id')

   #    # Filter data yang sudah ada
   #    existing_ids = existing_jabatan_ids.ids

   #    # Buat domain untuk menyaring nilai-nilai yang sudah dipilih sebelumnya
   #    for record in self:
   #       record.jabatan_id = False
   #       record.jabatan_id_domain = [('id', 'not in', existing_ids)]

   # jabatan_id_domain = fields.Many2many('jabatan', compute='_compute_jabatan_id', store=False)
   
   # @api.model
   # def _get_domain_other_model_id(self):
   #    # Ambil semua nilai dari field Many2one 'other_model_id'
   #    existing_other_model_ids = self.env['instruktur'].search([]).mapped('jabatan_id')

   #    # Buat domain untuk menyaring nilai-nilai yang sudah dipilih sebelumnya
   #    domain = [('jabatan_id', 'not in', existing_other_model_ids.ids)]

   #    return domain
   # @api.constrains('jabatan_id')
   # def _check_jabatan_constraints(self):
   #    found_records = self.search([('field1', '=', search_value)])

   #    # Cek apakah data ditemukan atau tidak
   #    if found_records:
   #       # Data ditemukan
   #       return True
   #    else:
   #       # Data tidak ditemukan
   #       return False
      # for record in self:
      #    cek_staff = self.env['instruktur'].search(['jabatan_id.jenis_jabatan','not in','3']).mapped('jabatan_id')
      #    if len(cek_staff) > 1 or (len(cek_staff) == 1 and cek_staff.id != record.id):
      #       raise ValidationError("tes")
         
class Keahlian(models.Model):
   _name = 'keahlian'
   _description = 'Keahlian'

   name = fields.Char(string='Nama Keahlian', required=True)
   