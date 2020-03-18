# -*- coding: utf-8 -*-
from odoo import http

# class O3Payroll(http.Controller):
#     @http.route('/o3_payroll/o3_payroll/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/o3_payroll/o3_payroll/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('o3_payroll.listing', {
#             'root': '/o3_payroll/o3_payroll',
#             'objects': http.request.env['o3_payroll.o3_payroll'].search([]),
#         })

#     @http.route('/o3_payroll/o3_payroll/objects/<model("o3_payroll.o3_payroll"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('o3_payroll.object', {
#             'object': obj
#         })