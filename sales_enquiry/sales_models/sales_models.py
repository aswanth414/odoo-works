# - * - coding: utf - 8 -
# *-
from odoo import models, fields, api


class SalesEnquiry(models.Model):
    _name = 'sales.enquiry'
    _description = "Sales Enquiry Detais"
    customer = fields.Many2one('res.partner', string='Customer')
    enquiry_date = fields.Date(string="Enquiry Date")
    address = fields.Many2one(comodel_name="sale.order", string="Address")
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    enquiry_line_ids = fields.One2many('sales.enquiry.lines', 'enquiry_lines', string="Enquiry Line")

    @api.depends('quantity', 'price_unit')
    def compute_subtotal(self):
        for order in self:
            price_subtotal = 0.0
            for line in order.enquiry_line_ids:
                price_subtotal = line.quantity * line.price_unit
            line.price_subtotal = price_subtotal


class SalesEnquiryLine(models.Model):
    _name = 'sales.enquiry.lines'
    enquiry_lines = fields.Many2one('sales.enquiry', ondelete='cascade', string="SalesEnquiry", required=True)
    product_id = fields.Many2one('product.product', string='Product')
    description = fields.Text(string='Description')
    quantity = fields.Float(string="Quantity ")
    product_uom_id = fields.Many2one('uom.uom', 'Unit of Measure', required=True)
    price_unit = fields.Float(String='Unit Price', required=True, digits='Product Price', default=0.0)
    price_subtotal = fields.Float(compute='_compute_subtotal', string='Subtotal', store=True)

    # amount_total = fields.Float(string='Amount Total', readonly=True, store=True)

    # @api.depends('quantity', 'price_unit')
    # def compute_subtotal(self):
    #     for order in self:
    #         price_subtotal = 0.0
    #         for line in order.enquiry_line_ids:
    #             price_subtotal = line.quantity * line.price_unit
    #         line.price_subtotal += price_subtotal
