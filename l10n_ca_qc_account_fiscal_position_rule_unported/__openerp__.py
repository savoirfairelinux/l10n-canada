# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2010 - 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Account Fiscal Position Rules for Quebec, Canada",
    "version": "1.0",
    "author": "Savoir-faire Linux",
    "website": "http://www.savoirfairelinux.com",
    "license": "AGPL-3",
    "category": "Localization/Accounting",
    "description": """
Account Fiscal Position Rules for Quebec, Canada
================================================

This module adds the fiscal position rules to set the fiscal position of a
document (picking, invoice, sale order, purchase order) based on the canadian
province or territory.

Contributors
------------
* Jonatan Cloutier <jonatan.cloutier@savoirfairelinux.com>
* Sandy Carter <sandy.carter@savoirfairelinux.com>
""",
    "depends": [
        'account_fiscal_position_rule_sale',
        'account_fiscal_position_rule_purchase',
        'account_fiscal_position_rule_stock',
        'l10n_ca_toponyms',
        'l10n_ca',
    ],
    "data": [
        'rules.xml',
    ],
    "installable": False,
}
