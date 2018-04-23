# -*- coding: utf-8 -*-
from odoo import http

# class UniteKbTags(http.Controller):
#     @http.route('/unite_kb_tags/unite_kb_tags/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unite_kb_tags/unite_kb_tags/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unite_kb_tags.listing', {
#             'root': '/unite_kb_tags/unite_kb_tags',
#             'objects': http.request.env['unite_kb_tags.unite_kb_tags'].search([]),
#         })

#     @http.route('/unite_kb_tags/unite_kb_tags/objects/<model("unite_kb_tags.unite_kb_tags"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unite_kb_tags.object', {
#             'object': obj
#         })
