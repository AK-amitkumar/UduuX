# -*- coding: utf-8 -*-
from docutils.writers import odf_odt

from odoo import models, fields, api
from odoo.fields import Html


class Unite(models.Model):
    _name = 'unite.core'
    _description = 'UNITE Core'
    
    name = fields.Char()
    html = fields.Html('test')