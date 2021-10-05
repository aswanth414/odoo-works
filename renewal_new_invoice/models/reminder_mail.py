# -*- coding: utf-8 -*-
import datetime

from febnouaenewaddons import renewal_new_invoice
from odoo import models, fields, api
from datetime import date
from datetime import timedelta
from odoo.exceptions import UserError


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    _description = "Email Reminder"

    renewal_date = fields.Date(comodel_name="account.move.line", string="Reminder Date", readonly=True,
                               compute='_compute_renewal_date')

    end_date = fields.Date()
    email_reminder = fields.Boolean('Email Reminder')

    @api.depends('end_date')
    def _compute_renewal_date(self):
        for r in self:
            if not (r.end_date and r.start_date):
                r.renewal_date = False
            else:
                r.renewal_date = (r.end_date - timedelta(days=15))

    @api.model
    def get_email_to(self):
        user_group = self.env.ref("renewal_new_invoice.group_email_cc")
        email_list = [
            usr.partner_id.email for usr in user_group.users if usr.partner_id.email]
        return ",".join(email_list)

    @api.model
    def _sent_email_reminder(self):
        print("sending.............")
        reminder_template = self.env.ref('renewal_new_invoice.email_template_reminder_invoice').id

        template = self.env['mail.template'].browse(reminder_template)
        today = datetime.datetime.now()
        reminder_date = (today + timedelta(days=15))
        reminder_activities = self.env['account.move.line'].search([('end_date', '=', reminder_date)])
        if reminder_activities:
            print("today_month_day", today)
            print("reminder: ", reminder_activities)
            for i in reminder_activities:
                print(i)
                self.env['account.move.line'].browse(i)
                template.send_mail(i.id, force_send=True)
