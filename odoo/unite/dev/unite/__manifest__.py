# -*- coding: utf-8 -*-
{
    'name': "unite",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.odoo.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'UNITE',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'
        ,"unite_backend"
        ,"autostaging_base"
        ,"autostaging_project_task"
        ,"business_requirement"
        ,"business_requirement_deliverable"
        ,"business_requirement_deliverable_cost"
        ,"business_requirement_deliverable_crm"
        ,"business_requirement_deliverable_project"
        ,"business_requirement_deliverable_project_task_categ"
        ,"business_requirement_deliverable_resource_template"
        ,"business_requirement_deliverable_resource_template_categ"
        ,"project_model_to_task"
        ,"project_parent"
        ,"project_stage_closed"
        ,"project_stage_state"
        ,"project_task_category"
        ,"project_task_default_stage"
        ,"project_task_dependency"
        ,"project_task_order_kanban_state"
        ,"project_task_search_custom"
],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/core.xml',
        'views/project.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}