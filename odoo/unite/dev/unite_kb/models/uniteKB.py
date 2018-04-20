# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniteKB(models.Model):
    _name = 'unite_kb.UniteKB'
    _inherits = 'unite_kb_category'
    ArtTitle = fields.Char()
    Author = fields.One2many()
    CreatedAt = fields.Date()
    fields.date.today()
    Tags = fields.Many2one()
    Description = fields.Text()
    DevLang = fields.Many2one()
    Version = fields.Integer()
    Status = fields.Char()
    LastEditedBy = fields.One2many()
    LastEditedAt = fields.Date()
    fields.date.today()
    Problem = fields.Html()
    Symptoms = fields.Html()
    Solutions = fields.Html()
    Inform = fields.Many2one()


