# -*- coding: utf-8 -*-
from odoo import http

# class UniteClavem(http.Controller):
#     @http.route('/unite_clavem/unite_clavem/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unite_clavem/unite_clavem/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unite_clavem.listing', {
#             'root': '/unite_clavem/unite_clavem',
#             'objects': http.request.env['unite_clavem.unite_clavem'].search([]),
#         })

#     @http.route('/unite_clavem/unite_clavem/objects/<model("unite_clavem.unite_clavem"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unite_clavem.object', {
#             'object': obj
#         })