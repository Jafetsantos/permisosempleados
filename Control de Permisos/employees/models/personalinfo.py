from odoo import models, fields, api

class personalinfo(models.Model):

    _name = "employees.personalinfo"
    _description = "PersonalInformation"
    employee_id= fields.Many2one('employees.employees')
    name = fields.Char(string="Nombre Completo")
    correo = fields.Char(string="Correo Institucional")
    identidad = fields.Char(string="Numero Identidad")
    gender = fields.Char(string= "gender")
    municipio = fields.Char(string= "Municipio")
    departamento = fields.Char(string= "Departamento")
    tel = fields.Char(string= "tel")
    correoR = fields.Char(string= "correo de respaldo")
    employee_type = fields.Char(string= "Cargo")
    user_id= fields.Many2one('res.users',related='employee_id.user_id')
    