from odoo import models, fields

class SeguimientoPermiso(models.Model):
    
    _name = 'employees.seguimiento_empleado'
    #_inherit =['mail.thread']
    _description = 'Seguimiento de Permisos'
    seguimiento_id=fields.Many2one('res.users',related='employee_id.user_id')
    #FK
    employee_id= fields.Many2one('employees.employees',
                                default=lambda self: self._get_default_employee_id(),
                                readonly=True)
    user_id=fields.Many2one('res.users')
   
    nombre_empleado = fields.Char(
        string="Nombre del Empleado",
        default=lambda self: self._get_default_nombre_empleado(),
        readonly=True
    )
    puesto = fields.Char(
        string='Puesto de Trabajo',
        default=lambda self: self._get_default_puesto(),
        readonly=True
    )
    tipo_permiso = fields.Selection([
        ('vacaciones', 'Vacaciones'),
        ('enfermedad', 'Enfermedad'),
        ('otros', 'Otros')
    ], string="Tipo de Permiso",required=True)
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
            
    def _get_default_nombre_empleado(self):
        # Obtener el empleado asociado al usuario actual
        employee = self.env['employees.employees'].search([
            ('user_id', '=', self.env.uid)
        ], limit=1)
        return employee.name if employee else ''

    def _get_default_puesto(self):
        # Obtener el puesto del empleado asociado al usuario actual
        employee = self.env['employees.employees'].search([
            ('user_id', '=', self.env.uid)
        ], limit=1)
        return employee.employee_type if employee else ''        
    
    def _get_default_employee_id(self):
        # Obtener el empleado asociado al usuario actual
        employee = self.env['employees.employees'].search([
            ('user_id', '=', self.env.uid)
        ], limit=1)
        return employee.id if employee else False