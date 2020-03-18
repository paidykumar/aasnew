# -*- coding: utf-8 -*-
{
    'name': "o3_spr",

    'summary': """
        student Progress Report
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "o3 it enterprises",
    'website': "http://www.o3sol.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '12.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'openeducat_assignment', 'openeducat_exam'],

    # always loaded
    'data': [
        'report/student_progress.xml',
        'report/report_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}