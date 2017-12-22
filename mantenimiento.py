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

class mantenimiento(osv.Model):


    def _check_precio(self, cr, uid, ids):
        # Los servicios tienen que tener almenos 0.1 KM para poder registrarse
        serv=self.browse(cr, uid, ids[0],context=None)
        if serv.precio <= 0:
            return False
        return True

    _name = 'mantenimiento'
    _description = 'Clase para el mantenimiento de un autobus'

    _columns = {
            'name':fields.text('Descripcion'),
            'precio':fields.float('Precio', required=True),
            'fecha':fields.date('Fecha', required=True),
            'matricula_id':fields.many2one("autobus","Matricula"),
            'state':fields.selection([
                ('solicitado','Solicitado'),
                ('enmante','enMantenimiento'),
                ('finalizado','finalizado')], 'Estado', readonly=True, default='solicitado'),
        }


    _constraints = [(_check_precio, 'El precio del mantenimiento no puede ser menor de 0' , [ 'precio'])]
mantenimiento()
