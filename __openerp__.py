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
{
    "name": "Albus",
    "version": "1.0",
    "depends": ["base"],
    "author": "Equipo 02",
    "category": "Autobus",
    "description": """
    Modulo referente a la gestion del alquiler de autobuses.
    """,
    "init_xml": [],
    'data': ['autobus_view.xml', 'mantenimiento_view.xml', 'conductor_view.xml','vacaciones_view.xml','alquiler_view.xml','cliente_view.xml','apuntes_view.xml', 'cuenta_view.xml', 'servicio_view.xml','mantenimiento_workflow.xml','alquiler_workflow.xml'],
    'demo_xml': ['demo.xml'],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}
