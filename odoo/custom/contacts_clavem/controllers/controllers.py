# -*- coding: utf-8 -*-
from odoo import http

# class Clavem(http.Controller):
#     @http.route('/contacts_clavem/contacts_clavem/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contacts_clavem/contacts_clavem/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contacts_clavem.listing', {
#             'root': '/contacts_clavem/contacts_clavem',
#             'objects': http.request.env['contacts_clavem.contacts_clavem'].search([]),
#         })

#     @http.route('/contacts_clavem/contacts_clavem/objects/<model("contacts_clavem.contacts_clavem"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contacts_clavem.object', {
#             'object': obj
#         })