# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import osv
from osv import fields

class conductor(osv.Model):

    _name = 'conductor'
    _description = 'Informacion sobre los conductores'
 
    _columns = {
            'name':fields.char('DNI', size=9, required=True, readonly=False),
            'nombre':fields.char('Nombre', size=100, required=False, readonly=False),
            'apellidos':fields.char('Apellidos', size=100, required=False, readonly=False),
            'sexo':fields.selection((('h','Hombre'),('m','Mujer'),('x','Otro')),'Sexo'),
            'telefono':fields.integer('Telefono',required=False, readonly=False),
            'correo':fields.char('Correo', size=100, required=False, readonly=False),
            'direccion':fields.char('Direccion', size=100, required=False, readonly=False),
            'servicio_id':fields.one2many("servicio","conductor_id","Servicios"),
            'cuenta_id':fields.many2one('cuenta','Cuentas'),
            'vacacion_id':fields.many2many("vacaciones",'conductor_vacaciones_rel','conductor_id','vacacion_id','Vacaciones')
        }
    
    _sql_constraints = [('cuenta_uniq', 'unique (cuenta_id)', 'Esa cuenta corriente pertence a otro conductor'),]
    
conductor()