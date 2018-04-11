# -*- coding: utf-8 -*-
from odoo import http

# class UnitKnowledgeBase(http.Controller):
#     @http.route('/unit_knowledge_base/unit_knowledge_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unit_knowledge_base/unit_knowledge_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unit_knowledge_base.listing', {
#             'root': '/unit_knowledge_base/unit_knowledge_base',
#             'objects': http.request.env['unit_knowledge_base.unit_knowledge_base'].search([]),
#         })

#     @http.route('/unit_knowledge_base/unit_knowledge_base/objects/<model("unit_knowledge_base.unit_knowledge_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unit_knowledge_base.object', {
#             'object': obj
#         })