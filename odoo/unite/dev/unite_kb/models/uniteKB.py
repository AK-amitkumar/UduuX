# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniteKB(models.Model):
    _name = 'unite.kb'
    ArtTitle = fields.Char(string="ArtTitle")
    # Author = fields.One2many(comodel_name="Author", string="Author")
    CreatedAt = fields.Date(string="Date")
    fields.date.today()
    #Tags = fields.Many2one(comodel_name="Tags", string="Tags")
    Description = fields.Text(string="Description")
    #DevLang = fields.Many2one(comodel_name="DevLang")
    Version = fields.Integer(string="Version")
    Status = fields.Char(string="Status")
    #LastEditedBy = fields.One2many(string="LastEditedBy")
    LastEditedAt = fields.Date(string="LastEditedAt")
    fields.date.today()
    Problem = fields.Html(string="Problem")
    Symptoms = fields.Html(string="Symptoms")
    Solutions = fields.Html(string="Solutions")
    #Inform = fields.Many2one(string="Inform")
