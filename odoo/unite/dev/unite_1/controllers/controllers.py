# -*- coding: utf-8 -*-
from odoo import http

# class Unite1(http.Controller):
#     @http.route('/unite_1/unite_1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unite_1/unite_1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unite_1.listing', {
#             'root': '/unite_1/unite_1',
#             'objects': http.request.env['unite_1.unite_1'].search([]),
#         })

#     @http.route('/unite_1/unite_1/objects/<model("unite_1.unite_1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unite_1.object', {
#             'object': obj
#         })