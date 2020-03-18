# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': "o3_sessions",
    'version': '12.0.1.0.0',

    'summary': """
        it is extension of openeducat_timetable module .....""",

    'description': """
        Long description of module's purpose
    """,

    'author': "O3 it enterprises",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',


    # any module necessary for this one to work correctly
    'depends': ['openeducat_timetable', 'base', 'openeducat_exam'],

    # always loaded
    'data': ['report/o3_timetable_student_generate.xml',
             'report/o3_timetable_teacher_generate.xml',
             'wizard/time_table_report.xml',
             'report/report_menu.xml',
             'menus/op_menu.xml'],
    # only loaded in demonstration mode
    'demo': [

    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}