# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SalesEnquiryConfirm(models.TransientModel):
    _name = "sales.enquiry.confirm"

    def action_wizard_confirm_draft(self):
        sales_enquiry = self.env['sales.enquiry'].browse(self._context.get('active_ids', []))
        for record in sales_enquiry:
            if record.state == 'new':
                sales_enquiry.action_confirm()

