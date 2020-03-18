# -*- coding: utf-8 -*-
{
    'name': "o3_assignments",

    'summary': """
        adding a report to assignments to display assignment results""",

    'description': """
        Long description of module's purpose
    """,

    'author': "o3 it enterprises",
    'website': "http://www.o3sol.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'openeducat_assignment'],

    # always loaded
    'data': [
        #'views/portal_assignment_submission.xml',
        'wizard/assignments_wizard.xml',
        'report/assignment_report.xml',
        'report/report_menu.xml',
        'menus/op_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}