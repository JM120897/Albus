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
#    This program is distributed in the hope that it will be useful,[]
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
    
    #Intento de constraint funcional
    def _check_cuenta(self, cr, uid, ids, context=None):
        conductor = self.browse(cr, uid, ids[0], context=None) 
        cuenta = conductor.cuenta_id
        #if(len(cuenta.cliente_id) > 0):
        if(cuenta.cliente_id is not None):
            return False
        else:
            return True
    
    def quitarVacaciones(self, cr, uid, ids, context=None):
        res = self.write(cr, uid, ids, {'vacacion_id':[(5, )]}, context=None)
        return res

    _name = 'conductor'
    _description = 'Informacion sobre los conductores'

    _columns = {
            'name':fields.char('DNI', size=9, required=True, readonly=False),
            'nombre':fields.char('Nombre', size=100, required=False, readonly=False),
            'apellidos':fields.char('Apellidos', size=100, required=False, readonly=False),
            'sexo':fields.selection((('h','Hombre'),('m','Mujer'),('x','Otro')),'Sexo'),
            'telefono':fields.integer('Telefono', required=False, readonly=False),
            'correo':fields.char('Correo', size=100, required=False, readonly=False),
            'direccion':fields.char('Direccion', size=100, required=False, readonly=False),
            'servicio_id':fields.one2many("servicio","conductor_id","Servicios"),
            'cuenta_id':fields.many2one('cuenta','Cuentas'),
            'vacacion_id':fields.many2many("vacaciones",'conductor_vacaciones_rel','conductor_id','vacacion_id','Vacaciones')
        }

    #_constraints = [(_check_cuenta, 'Esa cuenta pertenece a un cliente' , [ 'cuenta_id'])]
    _sql_constraints = [('dni_uniq_conductor', 'unique (name)', 'Ya existe un usuario con ese DNI'),]
    _sql_constraints = [('cuenta_uniq_conductor', 'unique (cuenta_id)', 'Esa cuenta corriente pertence a otro conductor'),]

conductor()
