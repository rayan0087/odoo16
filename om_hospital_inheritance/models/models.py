# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class om_hospital_inheritance(models.Model):
#     _name = 'om_hospital_inheritance.om_hospital_inheritance'
#     _description = 'om_hospital_inheritance.om_hospital_inheritance'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
