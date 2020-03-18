# -*- coding: utf-8 -*-
from odoo import http

# class O3Parents(http.Controller):
#     @http.route('/o3_parents/o3_parents/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/o3_parents/o3_parents/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('o3_parents.listing', {
#             'root': '/o3_parents/o3_parents',
#             'objects': http.request.env['o3_parents.o3_parents'].search([]),
#         })

#     @http.route('/o3_parents/o3_parents/objects/<model("o3_parents.o3_parents"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('o3_parents.object', {
#             'object': obj
#         })