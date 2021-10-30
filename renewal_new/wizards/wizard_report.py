# -*- coding: utf-8 -*-
from odoo import models, fields, api
#from datetime import datetime as dt
class Reportwizzard(models.TransientModel):
    _name = "renewal.report.wizard"

    end_date = fields.Date(String="End Date")
    products = fields.Many2one('product.product', string='Product')
    domain_ids = fields.Many2one("domain.inherit", string='Subs Item')

    def action_print_renewal_report(self):
        domain = []
        # products=self.products
        domain_ids = self.domain_ids
        if domain_ids:
            domain += [('domain_ids', '=', domain_ids.id)]
        end_date = self.end_date
        if end_date:
            domain += [('end_date', '=', end_date)]
        # print("Test....!",self.read()[0])
        reports = self.env['account.move.line'].search_read(domain)
        # print('reports', reports)
        data = {
            'form': self.read()[0],
            'reports': reports,
        }
        return self.env.ref('renewal_new.report_renewal').report_action(self, data=data)
