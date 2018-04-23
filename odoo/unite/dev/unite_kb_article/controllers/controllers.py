# -*- coding: utf-8 -*-
from odoo import http

# class UniteKb(http.Controller):
#     @http.route('/unite_kb_article/unite_kb_article/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unite_kb_article/unite_kb_article/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unite_kb.listing', {
#             'root': '/unite_kb_article/unite_kb_article',
#             'objects': http.request.env['unite_kb_article.unite_kb_article'].search([]),
#         })

#     @http.route('/unite_kb_article/unite_kb_article/objects/<model("unite_kb_article.unite_kb_article"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unite_kb.object', {
#             'object': obj
#         })