# -*- coding: utf-8 -*-
from odoo import http

# class O3Fees(http.Controller):
#     @http.route('/o3_admissions_fees/o3_admissions_fees/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/o3_admissions_fees/o3_admissions_fees/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('o3_admissions_fees.listing', {
#             'root': '/o3_admissions_fees/o3_admissions_fees',
#             'objects': http.request.env['o3_admissions_fees.o3_admissions_fees'].search([]),
#         })

#     @http.route('/o3_admissions_fees/o3_admissions_fees/objects/<model("o3_admissions_fees.o3_admissions_fees"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('o3_admissions_fees.object', {
#             'object': obj
#         })