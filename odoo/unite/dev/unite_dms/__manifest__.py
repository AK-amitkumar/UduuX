# -*- coding: utf-8 -*-
{
    'name': "unite_dms",

    'summary': """
        MUK_DMS and Odoo Documents combination by UNITE""",

    'description': """
        MUK_DMS and Odoo Documents combination by UNITE
    """,

    'author': "UNITE",
    'contributors': 'Nik Istrefi',
    'website': "http://www.uniteit.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'UNITE',
    'version': '2018.10.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'muk_dms_access',
        'muk_dms_field',
        'muk_dms_file',
        'muk_attachment_lobject',
        'muk_fields_lobject',
        'muk_web_client',
        'muk_web_client_notification',
        'muk_web_export_attachment',
        'muk_web_glyphicons',
        'muk_web_preview_attachment',
        'muk_web_preview_audio',
        'muk_web_preview_csv',
        'muk_web_preview_image',
        'muk_web_preview_mail',
        'muk_web_preview_markdown',
        'muk_web_preview_msoffice',
        'muk_web_preview_text',
        'muk_web_preview_vector',
        'muk_web_preview_video',
        'muk_web_view_hierarchy',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}


