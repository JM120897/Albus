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

class cliente(osv.Model):
    
    #Intento de check de cuenta que no llego a funcionar
    def _check_cuenta(self, cr, uid, ids, context=None):
        cliente = self.browse(cr, uid, ids[0], context=None) 
        for cuenta in cliente.cuenta_id:
            if(cuenta.conductor_id is not None):
                return False
            else:
                return True

    _name = 'cliente'
    _description = 'Informacion sobre Cliente'
 
    _columns = {
        'name':fields.char('DNI', size=9, required=True, readonly=False),
        'nombre':fields.char('Nombre', size=100, required=True, readonly=False),
        'apellidos':fields.char('Apellidos', size=100, required=True, readonly=False),
        'telefono':fields.integer('Telefono', required=True),
        'correo':fields.char('Correo', size=100, required=True, readonly=False),
        'cuenta_id':fields.many2many('cuenta','cuenta_cliente_rel','cliente_id','cuenta_id','Cuentas'),
        'alquiler_id':fields.one2many("alquiler","cliente_id","Alquileres")
        }
    #_constraints = [(_check_cuenta, 'Alguna de las cuentas pertenece a un conductor' , [ 'cuenta_id'])]
    _sql_constraints = [('dni_uniq_cliente', 'unique (name)', 'Ya existe un usuario con ese DNI'),]
    
cliente()