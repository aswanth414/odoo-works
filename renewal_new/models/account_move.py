# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    end_customer = fields.Many2one('res.partner', string='End Customer')

    renewal_line_ids = fields.One2many('account.move.line', 'move_id',
                                       domain=[('exclude_from_invoice_tab', '=', False)],
                                       copy=False,)

    def action_post(self):
        result = super(AccountMove, self).action_post()
        renewal_ids = self.renewal_line_ids.renewal_ids
        # print("In post: renewal_ids= ", renewal_ids)
        if renewal_ids:
            renewal_ids.status_id = 'b'
        return result

