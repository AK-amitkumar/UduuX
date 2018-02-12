# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniteToolsDrawerFrame(models.Model):
    _name = 'unite.tools.drawer.iframe'
    _description = 'First Integration of Tools.Drawer by UNITE'

    name = fields.Char()
    htmlField = fields.Html(string="htmlContent")
