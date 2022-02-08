from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'
    _description = "Invoicing Disc"

    discount = fields.Float(String='Discount')

    def button_updates(self):
        for line in self.invoice_line_ids:
            line.discount = self.discount

    # def _move_autocomplete_invoice_lines_values(self):
    #     disc =super(AccountMove, self)._move_autocomplete_invoice_lines_values()
    #     # for line in self.invoice_line_ids:
    #     #     line.discount = self.discount
    #     disc['discount'] = self.discount
    #     # return disc





