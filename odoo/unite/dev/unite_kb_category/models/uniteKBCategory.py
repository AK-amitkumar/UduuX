# -*- coding: utf-8 -*-

###
# UNITE(c)
# This Class handles the tables and the logic of the Unite Knowledge Base module
#
# @autor: UNITE
###

from odoo import models, fields, api


class uniteKBCategory(models.Model):
    _name = 'unite.kb.category'
    _inherit = 'unite.kb'
    _description = 'The Category Extension of Unite Knowledge Base'

    categoryTitle = fields.Char(string="Category Title")
    subCategory = fields.Many2one("unite.kb", string="Sub-Category")
    masterCategory = fields.Many2one("unite.kb", string="Master-Category")
    customer = fields.Many2one('res.partner', string="Customer")
    forCustomer = fields.Boolean(string="isPublic")
    catTags = fields.Many2one("unite.kb")
    catOwner = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.user)
