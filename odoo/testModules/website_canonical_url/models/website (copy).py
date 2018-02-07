# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo Addon, Open Source Management Solution
#    © initOS GmbH 2016
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

from odoo import models, api
from odoo.http import request
from urlparse import urlparse, urlunparse


class website(models.Model):
    _inherit = 'website'

    @api.multi
    def get_canonical_url(self, req=None):
        canonical_url = None
        if req is None:
            req = request
        if req and req.httprequest.path:
            lang = self.env.lang
            if lang == request.website.default_lang_code:
                #canonical_url = req.httprequest.path               # Default - kurze URL /blog/neuigkeiten-1
                canonical_url = req.httprequest.base_url            # EQ: komplette URL http://localhost:8069/blog/neuigkeiten-1
            else:
                #url_parts = urlparse(req.httprequest.path)         # Default - kurze URL /blog/neuigkeiten-1
                url_parts = urlparse(req.httprequest.base_url)      # EQ: komplette URL http://localhost:8069/blog/neuigkeiten-1
                url_parts = list(url_parts)
                # change the path of the url
                url_parts[2] = lang + url_parts[2]
                canonical_url = urlunparse(url_parts)
        # Special case for rerouted requests to root path
        try:
            if (canonical_url.startswith("/page/") and
                    self.menu_id.child_id[0].url == canonical_url):
                canonical_url = "/"
        except:
            pass
        return canonical_url