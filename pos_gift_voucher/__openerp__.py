# -*- coding: utf-8 -*-

##############################################################################
#
#    This module copyright :
#        (c) 2015 VMCloud Solution (http://vmcloudsolution.pe)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Pos Gift Voucher',
    'version': '0.1',
    'category': 'Point Of Sale',
    'description': """
        Gift Voucher for Point of Sale
        """,
    'author': 'VMCloud Solution',
    'website': 'http://vmcloudsolution.pe',
    'depends': ['point_of_sale', 'pos_payment_return_id'],
	'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'pos_gift_voucher.xml',
        'views/templates.xml',
    ],
    'qweb':[
        'static/src/xml/pos.xml',
    ],
    'init_xml': [],
    'update_xml': [],
    'demo_xml': [],
    'test': [],
    'installable': True,
}
