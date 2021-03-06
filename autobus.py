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

class autobus(osv.Model):


    def _check_asientos(self, cr, uid, ids):
        # Los servicios tienen que tener almenos 0.1 KM para poder registrarse
        bus=self.browse(cr, uid, ids[0],context=None)
        if bus.numAsientos <=11:
            return False
        return True
    
    def _numero_servicios(self, cr, uid, ids, field, args, context=None):
        servicios = 0
        
        for autobus in self.browse(cr, uid, ids, context = context):
            servicios = len(autobus.servicio_id)
            
        return servicios

    def onchange_consumo(self,cr,uid,ids,consum,context=None):
        consumoMinimo=1.00;
        if consum < consumoMinimo:
            res = {
                'value' : {
                        'consumo':consumoMinimo
                }
            }
        elif consum > consumoMinimo:
                res = {
                    'value' : {
                            'consumo':consum
                    }
                }
        return res
    _name = 'autobus'
    _description = 'Informacion sobre autobus'

    _columns = {
            'name':fields.char('Matricula', size=8, required=True, readonly=False),
            'numAsientos':fields.integer('Numero de Plazas', required=True),
            'modelo':fields.char('Modelo de Autobus', size=32, required=False, readonly=False),
            'consumo':fields.float('Consumo (L/Km)',required=True),
            'revisado':fields.boolean('Necesita Revision'), #Cada mes este atributo pasara a FALSE
            'mantenimiento_id':fields.one2many("mantenimiento","matricula_id","Mantenimientos"),
            'servicio_id':fields.one2many("servicio","matricula_id","Servicios"),
            'numServicios':fields.function(_numero_servicios, type='integer', string="Número de Servicios", store=True)
        }


    _constraints = [(_check_asientos, 'El numero de asientos no pueden ser negativos' , [ 'numAsientos'])]
    _sql_constraints = [('matricula_uniq', 'unique (name)', 'Ya existe un autobus con esa matricula'),]


autobus()
