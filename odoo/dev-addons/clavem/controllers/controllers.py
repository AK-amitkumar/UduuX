# -*- coding: utf-8 -*-
from odoo import http

# class Clavem(http.Controller):
#     @http.route('/clavem/clavem/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clavem/clavem/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clavem.listing', {
#             'root': '/clavem/clavem',
#             'objects': http.request.env['clavem.clavem'].search([]),
#         })

#     @http.route('/clavem/clavem/objects/<model("clavem.clavem"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clavem.object', {
#             'object': obj
#         })