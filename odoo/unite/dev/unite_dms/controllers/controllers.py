# -*- coding: utf-8 -*-
from odoo import http

# class UniteDms(http.Controller):
#     @http.route('/unite_dms/unite_dms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unite_dms/unite_dms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unite_dms.listing', {
#             'root': '/unite_dms/unite_dms',
#             'objects': http.request.env['unite_dms.unite_dms'].search([]),
#         })

#     @http.route('/unite_dms/unite_dms/objects/<model("unite_dms.unite_dms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unite_dms.object', {
#             'object': obj
#         })