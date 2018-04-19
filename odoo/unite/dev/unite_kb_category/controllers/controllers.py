# -*- coding: utf-8 -*-
from odoo import http

# class UniteKbCategory(http.Controller):
#     @http.route('/unite_kb_category/unite_kb_category/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unite_kb_category/unite_kb_category/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unite_kb_category.listing', {
#             'root': '/unite_kb_category/unite_kb_category',
#             'objects': http.request.env['unite_kb_category.unite_kb_category'].search([]),
#         })

#     @http.route('/unite_kb_category/unite_kb_category/objects/<model("unite_kb_category.unite_kb_category"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unite_kb_category.object', {
#             'object': obj
#         })