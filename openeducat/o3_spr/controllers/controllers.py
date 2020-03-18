# -*- coding: utf-8 -*-
from odoo import http

# class O3StudentProgressReport(http.Controller):
#     @http.route('/o3_spr/o3_spr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/o3_spr/o3_spr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('o3_spr.listing', {
#             'root': '/o3_spr/o3_spr',
#             'objects': http.request.env['o3_spr.o3_spr'].search([]),
#         })

#     @http.route('/o3_spr/o3_spr/objects/<model("o3_spr.o3_spr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('o3_spr.object', {
#             'object': obj
#         })