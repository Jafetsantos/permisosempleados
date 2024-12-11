# -*- coding: utf-8 -*-
# from odoo import http

#controlador para login permisos empleados


from odoo import http
from odoo.http import request

class CustomLogin(http.Controller):

    @http.route('/employees/login', type='http', auth="public", website=True, methods=['POST'])
    def login(self, email, password):
        # Validar usuario
        user = request.env['employees.user_id'].sudo().search([('email', '=', email), ('password', '=', password)], limit=1)
        if user:
            # Establecer la sesión personalizada
            request.session['employees_user_id'] = user.id
            return http.local_redirect('/employees/personalinfo')
        else:
            return request.render('custom_module.login', {'error': 'Correo o contraseña incorrectos'})

   






# class Employees(http.Controller):
#     @http.route('/employees/employees', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employees/employees/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employees.listing', {
#             'root': '/employees/employees',
#             'objects': http.request.env['employees.employees'].search([]),
#         })

#     @http.route('/employees/employees/objects/<model("employees.employees"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employees.object', {
#             'object': obj
#         })

