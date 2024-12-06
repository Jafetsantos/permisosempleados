# -*- coding: utf-8 -*-
# from odoo import http


# class Seguimiento(http.Controller):
#     @http.route('/seguimiento/seguimiento', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/seguimiento/seguimiento/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('seguimiento.listing', {
#             'root': '/seguimiento/seguimiento',
#             'objects': http.request.env['seguimiento.seguimiento'].search([]),
#         })

#     @http.route('/seguimiento/seguimiento/objects/<model("seguimiento.seguimiento"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('seguimiento.object', {
#             'object': obj
#         })

