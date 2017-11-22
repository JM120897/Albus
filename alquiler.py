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

class alquiler(osv.Model):

    _name = 'alquiler'
    _description = 'Informaci�n sobre los alquileres'
 
    _columns = {
            'name':fields.char('name', size=64, required=True, readonly=False),
            'id':fields.char('id', size=64, required=True, readonly=False),
            'horas':fields.integer('Horas de alquiler',required=False, readonly=False),
            'fecha':fields.date('Fecha', required=False, readonly=False),
            'numPersonas':fields.integer('Numero de personas',required=False, readonly=False),
            'descripcion':fields.char('Descripcion', size=150, required=False, readonly=False),
            'lugarOrigen':fields.char('Lugar de Origen', size=64, required=False, readonly=False),
            'lugarDestino':fields.char('Lugar de Destino', size=64, required=False, readonly=False),
            
        }
alquiler()