# -*- coding: utf-8 -*-
from odoo import http

# class UniteEducation(http.Controller):
#     @http.route('/unite_education/unite_education/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unite_education/unite_education/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unite_education.listing', {
#             'root': '/unite_education/unite_education',
#             'objects': http.request.env['unite_education.unite_education'].search([]),
#         })

#     @http.route('/unite_education/unite_education/objects/<model("unite_education.unite_education"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unite_education.object', {
#             'object': obj
#         })