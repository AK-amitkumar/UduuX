# -*- coding: utf-8 -*-
{
    'name': "UNITE Drawer",

    'summary': """
        UNITE simple draw.io integration
    """,

    'description': """
        Modeling tool
    """,

    'author': "UNITE",
    'contributors': "Nik Istrefi UNITE",
    'website': "http://www.untieit.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'UNITE',
    'version': '2018.10.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'application': True,
    'installable': True,
}