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

class vacaciones(osv.Model):

    def _check_dates(self, cr, uid, ids):
        # Los servicios tienen que tener almenos 0.1 KM para poder registrarse
        fecha=self.browse(cr, uid, ids[0],context=None)
        if fecha.fechaIni == fecha.fechaFin:
            return False
        return True

    _name = 'vacaciones'
    _description = 'Informacion sobre los vacaciones'



    _columns = {
            'name':fields.char('ID', size=150, required=False, readonly=False),
            'descripcion':fields.text('Descripcion'),
            'fechaIni':fields.date('Fecha Inicio', required=False, readonly=False),
            'fechaFin':fields.date('Fecha Fin', required=False, readonly=False),
            'conductor_id':fields.many2many('conductor','conductor_vacaciones_rel','vacacion_id','conductor_id','Conductores')
        }

    _constraints = [(_check_dates, 'Las vacaciones no pueden empezar y terminar el mismo dia', ['fechaIni'] )]
    _sql_constraints = [('id_uniq_vacaciones', 'unique (name)', 'Ya existe una entrada de vacaciones con el mismo ID'),]
    
vacaciones()
