# -*- coding: utf-8 -*-
# Copyright 2016, 2017 Openworx
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "UNITE Backend Theme",
    "summary": "Odoo 10.0 backend theme",
    "version": "2018.0.0.1",
    "category": "Themes/Backend",
    "website": "http://www.uniteit.ch",
	"description": """
		Unite Backend Theme, based on OpenWorkx Backend
    """,
	'images':[
        'images/screen.png'
	],
    "author": "UNITE",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
	'web_responsive',
    ],
    "data": [
        'views/assets.xml',
        'views/res_company_view.xml',
        'views/users.xml',
        'views/sidebar.xml',
    ],
}

