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
    _rec_name = 'uniteKbCategory'
    _description = 'The Category Extension of Unite Knowledge Base'

    categoryTitle = fields.Char(string="Category Title")
	# relDevision = fields.Many2one(string="Devision", ) TODO: clearify and implement this field
	subCategory = fields.Many2one(comodel_name="unite.kb.category",string="Sub-Category")
	masterCategory = fields.Many2one(comodel_name="unite.kb.category", string="Master-Category")
	customerFriendly = fields.Boolean(string="Customer Friendly")
	catTags = fields.Many2one(comodel_name="unite.kb.category")
	catOwner = fields.Many2one(comodel_name="hr")