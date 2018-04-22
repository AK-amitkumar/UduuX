# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniteKB(models.Model):
    _name = 'unite.kb'
    ArtTitle = fields.Char(string="ArtTitle")
    #Author = fields.One2many(comodel_name="res.users", string="Author")
    Author = fields.Char(string="Author")
    CreatedAt = fields.Date(string="Date")
    fields.date.today()
    #Tags = fields.Many2one(string="Tags")
    Description = fields.Text(string="Description")
    #DevLang = fields.Many2one(comodel_name="DevLang")
    Version = fields.Integer(string="Version")
    Status = fields.Char(string="Status")
    LastEditedBy = fields.Char(string="LastEditedBy")
    LastEditedAt = fields.Date(string="LastEditedAt")
    fields.date.today()
    Problem = fields.Html(string="Problem")
    Symptoms = fields.Html(string="Symptoms")
    Solutions = fields.Html(string="Solutions")
    Inform = fields.Many2one(string="Inform")


    @api.one
    def setAuthor(self):
        self.Author = self.env.user

    @api.onchange('Author')
    def onchange_method(self):
        self.LastEditedBy = self.Author
