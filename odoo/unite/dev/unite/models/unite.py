# -*- coding: utf-8 -*-

from odoo import models, fields, api

class unite(models.Model):
     _name = 'unite'
     _inherit = ''

     name = fields.Char()


     @api.depends('value')
     def _value_pc(self):
         self.value2 = float(self.value) / 100