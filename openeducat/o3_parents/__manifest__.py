# -*- coding: utf-8 -*-
{
    'name': "o3_parents",

    'summary': """
        added some new fields in openeducat_parent module""",

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
    'depends': ['base', 'openeducat_parent'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/o3_parents.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}