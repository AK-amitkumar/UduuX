# -*- coding: utf-8 -*-
from odoo import http

# class UniteApps(http.Controller):
#     @http.route('/unite_apps/unite_apps/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unite_apps/unite_apps/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unite_apps.listing', {
#             'root': '/unite_apps/unite_apps',
#             'objects': http.request.env['unite_apps.unite_apps'].search([]),
#         })

#     @http.route('/unite_apps/unite_apps/objects/<model("unite_apps.unite_apps"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unite_apps.object', {
#             'object': obj
#         })