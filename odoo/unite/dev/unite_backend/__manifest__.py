# -*- coding: utf-8 -*-
# Copyright 2016 Openworx, LasLabs Inc.
# Copyright 2017 Edi Santoso <repodevs@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "UNITE Backend Theme - Green",
    "summary": "Odoo 10.0 Theme",
    "version": "10.2018.0.0.1",
    "category": "Themes/Backend",
    "website": "https://www.uniteit.ch",
	"description": """
        Backend theme for Odoo 10.0 Community Edition (based on Openworx Theme). More polished to match the green color.
		The app dashboard is based on the module web_responsive from LasLabs Inc and the theme on Bootstrap United.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "UNITE",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
    ],
    "data": [
        'views/assets.xml',
        'views/web.xml',
    ],
}

