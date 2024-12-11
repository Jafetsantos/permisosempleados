# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Employees(models.Model):
    
    _name = "employees.employees"
    _description = "Employee"

    name = fields.Char(string="Nombre Completo")
    identidad = fields.Char(string="Numero Identidad")
    password= fields.Char(string= "Contraseña", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Género")
    
    employee_type = fields.Selection([
            ('admin', 'admin'),
            ('worker', 'Worker'),
            ('jefe depto', 'jefe depto'),
        
        ], string='Cargo')
    Departamento_trabajo = fields.Selection([
            ('ADMISIONES Y REGISTRO', 'ADMISIONES REGISTRO'),
            ('MANTENIMIENTO', 'MANTENIMIENNTO'),
            ('RRHH', 'RRHH'),
            ('ADMINISTRACION', 'ADMINISTRACION'),
            ('BIBLIOTECAS DE RECURSOS DOCUMENTALES', 'BIBLIOTECAS DE RECURSOS DOCUMENTALES'),
            ('VOAE', 'VOAE'),
            ('DIRECCION', 'DIRECCION'),
            ('LOGISTICA', 'LOGISTICA'),
            ('REGISTRO', 'REGISTRO'),
            ('CIENCIAS POLITICAS Y DERECHOS HUMANOS', 'CIENCIAS POLITICAS Y DERECHOS HUMANOS'),
            ('CULTURA FISICA Y DEPORTES', 'CULTURA FISICA Y DEPORTES'),
            ('ECOLOGIA Y RECURSOS NATURALES', 'ECOLOGIA Y RECURSOS NATURALES'),
            ('FILOSOFIA', 'FILOSOFIA'),
            ('ESTADISTICA MATEMATICA', 'ESTADISTICA MATEMATICA'),
            ('HISTORIA', 'HISTORIA'),
            ('INFRAESTRUCTURA', 'INFRAESTRUCTURA'),
            ('INGENIERIA DE SISTEMAS', 'INGENIERIA DE SISTEMAS'),
            ('LICENCIATURA COMERCIO INTERNACIONAL', 'LICENCIATURA COMERCIO INTERNACIONAL'),
            ('INGENIERIA CIENCIAS ACUICOLAS Y RECURSO MARINO COSTERO', 'INGENIERIA CIENCIAS ACUICOLAS Y RECURSO MARINO COSTERO'),
            ('lICENCIATURA EN ADMINISTRACION DE EMPRESAS', 'lICENCIATURA EN ADMINISTRACION DE EMPRESAS'),
            ('LICENCIAURA EN PEDAGOGIA', 'LICENCIATURA EN PEDAGOGIA'),
            ('INGENIERIA CIVIL', 'INGENIERIA CIVIL'),
            ('INGENIERIA ELECTRICA', 'INGENIERIA ELECTRICA'),
            ('INGENIERIA MECANICA', 'INGENIERIA MECANICA'),
            ('LENGUAS EXTRANJERAS', 'LENGUAS EXTRANJERAS'),
            ('LETRAS', 'LETRAS'),
            ('SOCIOLOGIA', 'SOCIOLOGIA'),
            ('MATEMATICA APLICADA', 'MATEMATICA APLICADA'),
            ('MATEMATICA PURA', 'MATEMATICA PURA'),
            ('MATERIA CONDENSADA', 'MATERIA CONDENSADA'),
        ], string='Departamento de trabajo')


    user_id=fields.Many2one('res.users')
    #datos de contacto

    municipio = fields.Char(string="Municipio")
    departamento  = fields.Char(string="Departamento")
    correo = fields.Char(string="Correo Institucional", required=True)
    correoR = fields.Char(string="Correo de respaldo")
    tel = fields.Char(string="phone number")
    img = fields.Binary(string="Empleado")

    def create(self, vals):
        record = super().create(vals)

        print ('-'*78, record)

        user = self.env['res.users'].sudo().create({
                'name': vals['name'],
                'login': vals['correo'],
                'email': vals['correo'],
                #'password': vals['password'],
                'active': True,
            })
        print(user)
        record.user_id = user.id
        user.with_context({'no_reset_password': True}).sudo().write({'password': vals['password']})
        #record.user_id.sudo().password = 'user.password '

        return record



