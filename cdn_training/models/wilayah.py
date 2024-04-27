from odoo import models, fields, api

class RefPropinsi(models.Model):
   _name        = 'ref.propinsi'
   _description = 'Ref Propinsi'

   name       = fields.Char(string='Nama Provinsi', required=True)
   kode       = fields.Char(string='Kode Provinsi')
   singkat    = fields.Char(string='Singkatan')
   keterangan = fields.Text('Keterangan')
   kota_ids   = fields.One2many(comodel_name='ref.kota', inverse_name='propinsi_id', string='Daftar Kota')

class RefKota(models.Model):
   _name        = 'ref.kota'
   _description = 'Ref Kota'

   name        = fields.Char(string='Nama Kota', required=True)
   propinsi_id = fields.Many2one(comodel_name='ref.propinsi', string='Nama Propinsi')
   kode        = fields.Char(string='Kode Kota')
   singkat     = fields.Char(string='Singkatan')
   keterangan  = fields.Text('Keterangan')
   kecamatan_ids = fields.One2many(comodel_name='ref.kecamatan', inverse_name='kota_id', string='Daftar Kecamatan')
   
class RefKecamatan(models.Model):
   _name = 'ref.kecamatan'
   _description = 'Ref Kecamatan'

   name = fields.Char(string='Nama Kecamatan', required=True)
   kode = fields.Char(string='Kode Kecamatan')
   keterangan = fields.Text('Keterangan')
   kota_id = fields.Many2one(comodel_name='ref.kota', string='Nama Kota')
   desa_ids = fields.One2many(comodel_name='ref.desa', inverse_name='kecamatan_id', string='Daftar Desa')
   
class RefDesa(models.Model):
   _name = 'ref.desa'
   _description = 'Ref Desa'

   name = fields.Char(string='Nama Desa')
   kode = fields.Char(string='Kode Desa')
   keterangan = fields.Text('Keterangan')
   kecamatan_id = fields.Many2one(comodel_name='ref.kecamatan', string='Nama Kecamatan')
   
   
   


