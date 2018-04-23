# -*- coding: utf-8 -*-
{
    'name': "UNITE Knowledge Base",

    'summary': """
        UNITE KB is a Knowledge Base and Manual/HowTo Management Module.
        """,

    'description': """
        comming soon
    """,

    'author': "UNITE",
    'website': "http://www.uniteit.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Knowledge',
    'version': '2018.0.1',

    # any module necessary for this one to work correctly
    'depends': ['unite'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'css': ['static/src/css/style.css'],
	'js': [ 'static/src/css/script.js' ],
	'images': [ 'images/src/img/image.png' ],

	'icon': 'static/src/img/icon.png',

    'application': True,
    'installable': True,
}