# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class seguimiento(models.Model):
#     _name = 'seguimiento.seguimiento'
#     _description = 'seguimiento.seguimiento'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

