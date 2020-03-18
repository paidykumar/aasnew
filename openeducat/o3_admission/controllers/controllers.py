# -*- coding: utf-8 -*-
from odoo import http

# class O3Admission(http.Controller):
#     @http.route('/o3_admission/o3_admission/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/o3_admission/o3_admission/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('o3_admission.listing', {
#             'root': '/o3_admission/o3_admission',
#             'objects': http.request.env['o3_admission.o3_admission'].search([]),
#         })

#     @http.route('/o3_admission/o3_admission/objects/<model("o3_admission.o3_admission"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('o3_admission.object', {
#             'object': obj
#         })