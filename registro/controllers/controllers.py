# -*- coding: utf-8 -*-
# from odoo import http


# class Registro(http.Controller):
#     @http.route('/registro/registro', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/registro/registro/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('registro.listing', {
#             'root': '/registro/registro',
#             'objects': http.request.env['registro.registro'].search([]),
#         })

#     @http.route('/registro/registro/objects/<model("registro.registro"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('registro.object', {
#             'object': obj
#         })

