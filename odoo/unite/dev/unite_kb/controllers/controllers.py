# -*- coding: utf-8 -*-
from odoo import http

# class UniteKb(http.Controller):
#     @http.route('/unite_kb/unite_kb/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unite_kb/unite_kb/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unite_kb.listing', {
#             'root': '/unite_kb/unite_kb',
#             'objects': http.request.env['unite_kb.unite_kb'].search([]),
#         })

#     @http.route('/unite_kb/unite_kb/objects/<model("unite_kb.unite_kb"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unite_kb.object', {
#             'object': obj
#         })