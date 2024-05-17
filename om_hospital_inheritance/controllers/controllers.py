# -*- coding: utf-8 -*-
# from odoo import http


# class OmHospitalInheritance(http.Controller):
#     @http.route('/om_hospital_inheritance/om_hospital_inheritance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_hospital_inheritance/om_hospital_inheritance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_hospital_inheritance.listing', {
#             'root': '/om_hospital_inheritance/om_hospital_inheritance',
#             'objects': http.request.env['om_hospital_inheritance.om_hospital_inheritance'].search([]),
#         })

#     @http.route('/om_hospital_inheritance/om_hospital_inheritance/objects/<model("om_hospital_inheritance.om_hospital_inheritance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_hospital_inheritance.object', {
#             'object': obj
#         })
