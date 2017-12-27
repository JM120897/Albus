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

class servicio(osv.Model):

    def _check_kilometers(self, cr, uid, ids):
        # Los servicios tienen que tener almenos 0.1 KM para poder registrarse
        serv=self.browse(cr, uid, ids[0],context=None)
        if serv.km <= 0:
            return False
        return True


    _name = 'servicio'
    _description = 'Informacion sobre el servicio'

    _columns = {
            'name':fields.char('ID', size=64, required=True, readonly=False),
            'descripcion':fields.text('Descripcion'),
            'km':fields.integer('Kilometros',required=False, readonly=False),
            'matricula_id':fields.many2one("autobus","Autobus"),
            'conductor_id':fields.many2one("conductor","Conductor"),
            'alquiler_id':fields.many2one("alquiler","Alquiler"),
        }

    _constraints = [(_check_kilometers, 'Kilometro no pueden ser negativos' , [ 'km'])]
    _sql_constraints = [('id_uniq_servicio', 'unique (name)', 'Ya existe un servicio con ese ID'),]

servicio()
