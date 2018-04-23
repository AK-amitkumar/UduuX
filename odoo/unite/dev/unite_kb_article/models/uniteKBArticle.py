# -*- coding: utf-8 -*-

from odoo import models, fields, api


class uniteKBArticle(models.Model):
    _name = 'unite.kb.article'
    _inherit = 'unite.kb'

    ArtTitle = fields.Char(string="ArtTitle")
    Author = fields.Many2one('res.users', 'Author', default=lambda self: self.env.user)
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
    Symptoms = fields.Html(string="Symptoms")
    Problem = fields.Char(string="Problem")
    Solutions = fields.Html(string="Solutions")
    Inform = fields.Many2many('res.users', string="many2many_tags")


    @api.one
    def setAuthor(self):
        self.Author = self.env.user

    @api.onchange('Author')
    def onchange_method(self):
        self.LastEditedBy = self.Author
