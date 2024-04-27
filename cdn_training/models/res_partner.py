from odoo import models, fields, api



class ResPartner(models.Model):
   _inherit = 'res.partner'

   jenis_kel = fields.Selection([('L', 'Laki Laki'), ('P','Perempuan')], string='Jenis Kelamin')
   propinsi_id = fields.Many2one(comodel_name='ref.propinsi', string='Provinsi')
   kota_id = fields.Many2one(comodel_name='ref.kota', string='Kota')
   kecamatan_id = fields.Many2one(comodel_name='ref.kecamatan', string='Kecamatan')
   desa_id = fields.Many2one(comodel_name='ref.desa', string='Desa/Keluarahan')
   