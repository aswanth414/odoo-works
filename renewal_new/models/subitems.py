# -*- coding: utf-8 -*-

from odoo import models, fields


class SubItems(models.Model):
    _inherit = 'domain.inherit'


    invoice_quantity = fields.Float(comodel_name='account.move.line', string='Invoiced Quantity',
                                    )
    purchase_quantity = fields.Float(string='Purchased Quantity')

    invoice_amount = fields.Float(string='Invoiced Amount')
    purchase_amount = fields.Float(string='Purchased Amount')
    result = fields.Float(string='Result', compute="_compute_invoiced_quantity")
    products = fields.Many2one('product.product', string='Product')
    active_sub = fields.Integer(String="Active Subitems")

    def _compute_invoiced_quantity(self):
        for lines in self:
            quantities = 0
            sum = 0
            bill_quantities = 0
            bill_sum = 0

            move_line_ids = self.env['account.move.line'].search([('move_id.type', '=', 'out_invoice'), ('move_id.state', '!=', 'cancel'), ('domain_ids', '=', lines.id)])
            # print(f'SUBITEMS.PY: move_line_ids of {lines.domain_ids}: {move_line_ids}')
            bill_move_line_ids = self.env['account.move.line'].search([('move_id.type', '=', 'in_invoice'), ('move_id.state', '!=', 'cancel'), ('domain_ids', '=', lines.id)])

            if move_line_ids:
                # print(f'SUBITEMS.PY: {len(move_line_ids)} MOVE LINES PRESENT for {lines.domain_ids}')
                for i in move_line_ids:
                    # print(f'subitems.py: i is {i.move_id.name}')
                    sum = sum + i.price_subtotal
                    quantities = quantities + i.quantity
                lines.invoice_quantity = quantities
                lines.invoice_amount = sum
            else:
                lines.invoice_quantity = 0.0
                lines.invoice_amount = 0.0

            if bill_move_line_ids:
                for i in bill_move_line_ids:
                    bill_sum = bill_sum + i.price_subtotal
                    bill_quantities = bill_quantities + i.quantity
                lines.purchase_quantity = bill_quantities
                lines.purchase_amount = bill_sum
            else:
                lines.purchase_quantity = 0.0
                lines.purchase_amount = 0.0
            lines.result = 0.0


