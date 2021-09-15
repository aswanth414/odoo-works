from datetime import timedelta
from odoo import models, fields, api


class Febnoship_Ship(models.Model):
    _name = 'febnoship.ship'
    _description = "shipping"

    ship_name = fields.Char(string="Ship Name", required=True)
    ship_number = fields.Integer(string="Ship Number")
    order_number = fields.Integer(string="Order Number")
    capacity = fields.Integer(string="Capacity")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date", compute='_compute_end_date')
    duration = fields.Float(string="Duration", digits=(6, 2), help="Duration in days")
    ship_line_ids = fields.One2many('febnoship.lines', 'order_line_ids', string="Order Lines")


    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
       for r in self:
         if not (r.start_date and r.duration):
            r.end_date = r.start_date
            continue

         duration = timedelta(days=r.duration, seconds=-1)
         r.end_date = r.start_date + duration

class Febnoship_Shiplines(models.Model):
    _name = 'febnoship.lines'
    _description = "shipping lines"

    order_line_ids = fields.Many2one('febnoship.ship', string="Order Number")
    order_name = fields.Char(string="Order Name", required=True)
    delivery_date = fields.Date(string="Delivery Date", default=fields.Date.today)
    expected_date = fields.Date(string="Expected Date", default=fields.Date.today)
    customer = fields.Char(string="Customer Name", required=True)
    website = fields.Char(string="Website")
    sales_person = fields.Char(string="Sales Person", required=True)
    company = fields.Char(string="Company", required=True)
    total = fields.Float(string="Total")
    invoice = fields.Char(string="Invoice")

