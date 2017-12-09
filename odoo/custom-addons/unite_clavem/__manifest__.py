# -*- coding: utf-8 -*-
{
    'name': "UNITE Clavem",

    'summary': """
        Clavem password manager
        """,

    'description': """
        Clavem is designed to manage passwords per contact/company/user.
    """,

    'author': "UNITE IT Solutions",
    'website': "http://www.uniteit.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '2017.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/clavem_views.xml',
        'views/templates.xml',
        'views/ucReports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}