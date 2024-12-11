# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Solicitud(models.Model):
    _inherit = "hr.leave"
    nombre=fields.Char()
   