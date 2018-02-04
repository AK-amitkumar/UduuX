# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Unite(models.Model):
    _name = 'unite.core'
    _description = 'UNITE Core'

    name = fields.Html