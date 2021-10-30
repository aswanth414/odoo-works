# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime as dt


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.onchange('product_id')
    def _default_subitem(self):
        product = self.product_id
        # print("product is", product)
        subitems = self.env['domain.inherit'].search([])
        if product:
            # print("Present: product is", product)
            for i in subitems:
                if i.products == product:
                    self.domain_ids = i.id

    quantity = fields.Float(string='Quantity')
    end_customer = fields.Many2one('res.partner', related='move_id.end_customer',
                                   string='End Customer')

    renewal_ids = fields.Many2one(comodel_name="account.move.line", string='Renewal', store=True,
                                  domain="[('move_id.state', '!=', 'cancel'),('domain_ids', '=', domain_ids)]")
    no_of_days = fields.Float(string="Number Of Days", compute='_duration', store=True)
    one_day_cost = fields.Float(string="One Day Cost", compute='_duration', store=True)

    domain_ids = fields.Many2one("domain.inherit", string='Subs Item', default=_default_subitem)
    status_id = fields.Selection(selection=[('active', 'Active'), ('a', 'Canceled'), ('b', 'Renewed'), ('c', 'Hold')],
                                 default='active', string='Status')

    @api.depends('start_date', 'end_date')
    def _duration(self):
        move = self[0].move_id
        # print("move is: ", move)
        for rec in self:
            # print("rec is: ", rec)
            if rec.start_date and rec.end_date:
                init_date = dt.strptime(str(rec.start_date), '%Y-%m-%d')
                ends_date = dt.strptime(str(rec.end_date), '%Y-%m-%d')
                rec.no_of_days = str((ends_date - init_date).days)
            else:
                rec.no_of_days = None
            if rec.no_of_days != 0.0:
                rec.one_day_cost = rec.price_subtotal / rec.no_of_days
                # print(f'rec.no.of days: {rec.no_of_days} and re.one_day_cost: {rec.one_day_cost}')
            else:
                rec.one_day_cost = None
        for i in move.renewal_line_ids:
            # print("i is: ", i)
            ii = i.id
            if not i.product_id and i.display_type not in ['line_section', 'line_note'] and type(ii) == int:
                # print("no prdct i is: ", i)
                i.exclude_from_invoice_tab = True

