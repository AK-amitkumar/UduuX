# -*- coding: utf-8 -*-

from odoo import models, fields, api


class unite_clavem(models.Model):
    _name = 'unite.clavem'

    descriptionAttr = fields.Char('Description', required=False)
    userNameAttr = fields.Char('Username', required=True)
    passwordAttr = fields.Char('Password', required=True)
    customerAttr = fields.Many2one('res.partner', 'Customer')
    refSysAttr = fields.Char('Related System', required=True)
    eMailAttr = fields.Char('eMail', required=False)
    infoAttr = fields.Text('Additional Information', required=False)
    isInternal = fields.Boolean('Internal Password', default=False)
#
