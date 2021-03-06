# -*- coding: utf-8 -*-
#    OpenERP, Open Source Management Solution
#    Copyright (c) Rooms For (Hong Kong) Limited T/A OSCG. All Rights Reserved.
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

from openerp import models, api, _, fields


class PurhcaseImportDefault(models.Model):
    _name = 'purchase.import.default'

    @api.onchange('company_id')
    def _onchange_company_id(self):
        self.supplier_invoice_journal_id = False
        self.supplier_payment_journal_id = False

    company_id = fields.Many2one('res.company', required=True, string='Company')
    invoice_method = fields.Selection([
        ('manual', 'Based on Purchase Order lines'),
        ('order', 'Based on generated draft invoice'),
        ('picking', 'Based on incoming shipments')],
        required=True, string='Invoicing Control')
    supplier_invoice_journal_id = fields.Many2one('account.journal', required=True, string='Supplier Invoice Journal')
    supplier_payment_journal_id = fields.Many2one('account.journal', required=True, string='Supplier Payment Journal')

    _sql_constraints = [
        ('name_company_uniq', 'unique(company_id)', 'Companies must be unique !'),
    ]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: