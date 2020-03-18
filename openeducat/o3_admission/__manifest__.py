# -*- coding: utf-8 -*-
{
    'name': "o3_admission",

    'summary': """
        extension of admission module""",

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
    'depends': ['base', 'openeducat_admission'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/o3_admission.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}