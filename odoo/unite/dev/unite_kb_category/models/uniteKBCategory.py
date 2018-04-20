# -*- coding: utf-8 -*-

###
# UNITE(c)
# This Class handles the tables and the logic of the Unite Knowledge Base module
#
# @autor: UNITE
###

from odoo import models, fields, api


class UniteKBCategory(models.Model):
    _name = 'unite.kb.category'
    _description = 'The Category Extension of Unite Knowledge Base'

    categoryTitle = fields.Char(string="Category Title")
    subCategory = fields.Many2one(comodel_name="unite.kb.category", string="Sub-Category")
    masterCategory = fields.Many2one(comodel_name="unite.kb.category", string="Master-Category")
    customerFriendly = fields.Boolean(string="Customer Friendly")
    catTags = fields.Many2one(comodel_name="unite.kb.category")
    catOwner = fields.Many2one(comodel_name="hr")

    @api.one
    def set_categoryTitle(self):
        self.categoryTitle = self

    @api.one
    def set_subCategory(self):
        self.subCategory = self

    @api.one
    def set_masterCategory(self):
        self.masterCategory = self

    @api.one
    def set_customerFriendly(self):
        self.customerFriendly = self

    @api.one
    def set_catTags(self):
        self.catTags = self

    @api.one
    def set_catOwner(self):
        self.catOwner = self

    
