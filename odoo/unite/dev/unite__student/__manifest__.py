# -*- coding: utf-8 -*-
{
    'name': "unite_Student",

    'summary': """
        This module will add a record to store student details""",

    'description': """
        This module will add a record to store student details
    """,

    'author': "Unite IT Solutions",
    'website': "http://www.uniteitsolutions.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'images': [
        "static/description/icon.png"
    ],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}