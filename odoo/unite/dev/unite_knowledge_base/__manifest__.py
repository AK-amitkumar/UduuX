# -*- coding: utf-8 -*-
{
    'name': "unit_knowledgeBase",

    'summary': """
        Knowledge Base Solution by UNITE""",

    'description': """
        KB by UNITE
    """,

    'author': "UNITE",
    'website': "https://www.uniteit.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '2018.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'document_page_work_instruction'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}