# -*- coding: utf-8 -*-
from odoo import http

# class O3Sessions(http.Controller):
#     @http.route('/o3__sessions/o3__sessions/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/o3__sessions/o3__sessions/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('o3__sessions.listing', {
#             'root': '/o3__sessions/o3__sessions',
#             'objects': http.request.env['o3__sessions.o3__sessions'].search([]),
#         })

#     @http.route('/o3__sessions/o3__sessions/objects/<model("o3__sessions.o3__sessions"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('o3__sessions.object', {
#             'object': obj
#         })