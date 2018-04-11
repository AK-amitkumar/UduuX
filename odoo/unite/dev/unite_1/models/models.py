# -*- coding: utf-8 -*-

from odoo import models, fields, api


class unite_1(models.Model):
    _name = 'unite_1.unite_1'

    name = fields.Char()
    surname = fields.Char()


@api.depends('value')
def _value_pc(self):
    self.value2 = float(self.value) / 100
