# -*- coding: utf-8 -*-
from odoo import http

# class O3Library(http.Controller):
#     @http.route('/o3_library/o3_library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/o3_library/o3_library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('o3_library.listing', {
#             'root': '/o3_library/o3_library',
#             'objects': http.request.env['o3_library.o3_library'].search([]),
#         })

#     @http.route('/o3_library/o3_library/objects/<model("o3_library.o3_library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('o3_library.object', {
#             'object': obj
#         })