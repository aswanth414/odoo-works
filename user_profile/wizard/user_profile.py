# - * - coding: utf - 8 -
# *-
from odoo import models, fields, api


class UserProfileWizzard(models.TransientModel):
    _name = 'user.profile.wizard'
    _description = "User Profile Creations"

    client = fields.Many2one('res.company', string='Primary Client')
    user_type = fields.Char()
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    email_id = fields.Char(string='Email Address')
    login_id = fields.Char(string='Login')
    pwd_id = fields.Char(string='Password')
