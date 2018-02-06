# -*- coding: utf-8 -*-
from odoo import http


class UniteStudent(http.Controller):
    @http.route('/test', auth='public')
    def index(self, **kw):
        return "Hello, world"
