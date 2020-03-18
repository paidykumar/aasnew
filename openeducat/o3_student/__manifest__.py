# -*- coding: utf-8 -*-
{
    'name': "o3_student",

    'summary': """
        extension of openeducat core module in students personal information""",

    'description': """
        Long description of module's purpose
    """,

    'author': "o3 it enterprises",
    'website': "http://www.o3sol.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'education',
    'version': '12.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'openeducat_core'],

    # always loaded
    'data': [
        'security/op_security.xml',
        'views/o3_student.xml',
        'views/portal_docs.xml',
        # 'menu/o3_menu.xml',
        # 'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}