from odoo import models, fields


class ResUsersGroup(models.Model):
    _inherit = "res.users"
    group_email_cc = fields.Boolean("Renewal Email CC", implied_group="renewal_new_invoice.group_email_cc")
