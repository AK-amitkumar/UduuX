# -*- coding: utf-8 -*-

from odoo import models, fields, api


class unite(models.Model):
    _name = 'unite.core'

    name = fields.Char()
    html = fields.Html()
