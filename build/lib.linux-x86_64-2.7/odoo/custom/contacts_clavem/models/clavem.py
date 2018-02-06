# -*- coding: utf-8 -*-

from odoo import models, fields, api


class contacts_clavem(models.Model):
    inherit = 'res.partners'

    userName = fields.Char('Username', required=True)
    password = fields.Char('Password', required=True)
    #cr
    info = fields.Text('Info')
