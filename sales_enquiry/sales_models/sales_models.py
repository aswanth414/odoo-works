# - * - coding: utf - 8 -
# *-
from odoo import models, fields, api


class SalesEnquiry(models.Model):
    _name = 'sales.enquiry'
    _description = "Sales Enquiry Detais"
    customer = fields.Many2one('res.partner', string='Customer')
    enquiry_date = fields.Date(string="Enquiry Date")
    address = fields.Many2one(comodel_name="res.partner", string="Address")
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    # currency_id = fields.Many2one("res.currency", string="Currency", required=True)
    enquiry_line_ids = fields.One2many('sales.enquiry.lines', 'enquiry_lines', string="Enquiry Line")
    note = fields.Text(string='Terms and condition')
    amount_total = fields.Float(string='Amount Total', readonly=True, store=True)


class SalesEnquiryLine(models.Model):
    _name = 'sales.enquiry.lines'
    enquiry_lines = fields.Many2one('sales.enquiry', ondelete='cascade', string="SalesEnquiry", required=True)
    product_id = fields.Many2one('product.product', string='Product')
    description = fields.Text(string='Description')
    quantity = fields.Float(string="Quantity ", default=1.0)
    product_uom_id = fields.Many2one('uom.uom', 'Unit of Measure', required=True)
    price_unit = fields.Float(String='Unit Price', required=True, digits='Product Price', default=0.0)
    price_subtotal = fields.Float(compute='_compute_total', string='Subtotal', store=True)

    @api.depends('quantity', 'price_unit', 'price_subtotal')
    def _compute_total(self):
        for order in self:
            price_subtotal = 0.0
            for line in order:
                price_subtotal = line.quantity * line.price_unit
            line.price_subtotal = price_subtotal
