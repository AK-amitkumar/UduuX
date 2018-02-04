# -*- coding: utf-8 -*-
from odoo import http

# class Unite(http.Controller):
#     @http.route('/unite/unite/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unite/unite/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unite.listing', {
#             'root': '/unite/unite',
#             'objects': http.request.env['unite.unite'].search([]),
#         })

#     @http.route('/unite/unite/objects/<model("unite.unite"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unite.object', {
#             'object': obj
#         })