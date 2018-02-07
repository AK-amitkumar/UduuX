# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo Addon, Open Source Management Solution
#    Copyright (C) 2014-now Equitania Software GmbH(<http://www.equitania.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, fields, api, _


class eq_res_company(models.TransientModel):
    _inherit = 'base.config.settings'

    @api.multi
    def get_default_eq_report_logo(self, fields):

        user = self.env['res.users'].browse(self._uid)
        found_company = False
        if user:
            found_company = user.company_id

        if found_company:
            result = found_company.eq_report_logo
            if result:
                return {'eq_report_logo': result}
        return {'eq_report_logo': None}

    @api.multi
    def set_eq_report_logo(self):
        for record in self:
            record.company_id.eq_report_logo = record.eq_report_logo

    eq_report_logo = fields.Binary('Company Report Logo')
