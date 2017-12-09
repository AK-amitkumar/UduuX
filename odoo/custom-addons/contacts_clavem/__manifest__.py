# -*- coding: utf-8 -*-
{
    'name': "contacts_clavem",

    'summary': """
        Clavem is a password manager.
    """,

    'description': """
        Clavem extends the base contacts module with password managing functionality.
        
        Developed by UNITE IT Solutions
        [n1k]
    """,

    'author': "Unite IT Solutions",
    'website': "http://www.uniteit.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '2017.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'contacts'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/clavem_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}