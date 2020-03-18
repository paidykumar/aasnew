# -*- coding: utf-8 -*-
from odoo import http

# class O3Health(http.Controller):
#     @http.route('/o3_health/o3_health/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/o3_health/o3_health/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('o3_health.listing', {
#             'root': '/o3_health/o3_health',
#             'objects': http.request.env['o3_health.o3_health'].search([]),
#         })

#     @http.route('/o3_health/o3_health/objects/<model("o3_health.o3_health"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('o3_health.object', {
#             'object': obj
#         })