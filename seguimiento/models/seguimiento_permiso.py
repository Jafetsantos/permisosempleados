from odoo import models, fields

class SeguimientoPermiso(models.Model):
    
    _name = 'seguimiento.permiso'
    _inherit =['mail.thread']
    _description = 'Seguimiento de Permisos'

    nombre_empleado = fields.Char(string="Nombre del Empleado", required=True)
    puesto = fields.Char(string="Puesto de Trabajo", required=True)
    tipo_permiso = fields.Selection([
        ('vacaciones', 'Vacaciones'),
        ('enfermedad', 'Enfermedad'),
        ('otros', 'Otros')
    ], string="Tipo de Permiso", required=True)
    fecha_solicitud = fields.Date(string="Fecha de Solicitud", default=fields.Date.context_today, readonly=True)
    fecha_inicio = fields.Date(string="Fecha de Inicio", required=True)
    fecha_fin = fields.Date(string="Fecha de Fin", required=True)
    motivo = fields.Text(string="Motivo", required=True)
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('proceso', 'En Proceso'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado')
    ], string="Estado", default='borrador', required=True, tracking=True)
    documentos = fields.Many2many('ir.attachment', string="Documentos Adjuntos")
    
    
    
    def action_drat_to_progress(self):
        print ('*' * 100)
        print (self)
        for rec in self:
            rec.estado = 'proceso'
            
            
    def action_progress_to_aprove(self):
        for record in self:
            record.write({'estado': 'aprobado'})
            
    def action_progress_to_reject(self):
        for record in self:
            record.write({'estado': 'rechazado'})
    
