# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.cli.scaffold import env
from odoo.unite.dev import unite__student


class UniteEducation(models.Model):
    _name = 'unite.education'
    _inherit = 'student.student'
    _description = 'We will add some extra fields to Stundents Module and mix informations between those two modules'

    name_class = fields.Char(string="Class-Name", required=False)
    # inheried field,changed to required 1
    student_gender = fields.Selection(string="Gender", selection=[('M', 'Male'), ('F', 'Female'), ], required=True)
    student_age = fields.Integer(string="Age", required=True)

    # new fields
    _html_field = fields.Html(string="TestHTML")

