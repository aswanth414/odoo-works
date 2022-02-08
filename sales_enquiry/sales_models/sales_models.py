# - * - coding: utf - 8 -
# *-
from odoo import models, fields, tools, api, _
from odoo.tools.misc import formatLang, get_lang


class SalesEnquiry(models.Model):
    _name = 'sales.enquiry'
    _description = "Sales Enquiry Details"

    customer = fields.Many2one('res.partner', string='Customer', required=True, )
    enquiry_date = fields.Date(string="Enquiry Date")
    address = fields.Many2one(comodel_name="res.partner", string="Address")
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    enquiry_line_ids = fields.One2many('sales.enquiry.lines', 'enquiry_lines', string="Enquiry Line")
    note = fields.Text(string='Terms and condition')
    amount_total = fields.Float(string='Amount Total', readonly=True, store=True, compute='_amount_total')
    sale_order_id = fields.Many2one('sale.order')
    name_seq = fields.Char(string="Sequence", required="True", copy="false", readonly="True", index="True",
                           default=lambda self: _("New"))

    state = fields.Selection([
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('quotation', 'Quotation Created'),
        ('cancel', 'Cancelled'),
        ('done', 'Done'),

    ], string='Status', readonly=True, default='new')

    @api.model
    def create(self, vals):

        if vals.get('name_seq', ('New')) == ('New'):
            if 'company_id' in vals:
                vals['name_seq'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code(
                    'end.service') or _('New')
            else:
                vals['name_seq'] = self.env['ir.sequence'].next_by_code('sales.enquiry.sequence') or _('New')

        result = super(SalesEnquiry, self).create(vals)
        return result

    def action_confirm(self):
        self.state = 'confirmed'

    def action_create_quotation(self):
        self.state = 'quotation'
        line_lst = []
        for record in self:

            for line in record.enquiry_line_ids:
                line_dic = {
                    'product_id': line.product_id.id,
                    'product_uom_qty': line.quantity,
                    'price_unit': line.price_unit,
                }
                line_lst.append((0, 0, line_dic))
            sale_vals = {
                'date_order': self.enquiry_date,
                'partner_id': self.customer.id,

                'order_line': line_lst
            }
            sale_id = self.env['sale.order'].create(sale_vals)
            print(sale_id)
            self.sale_order_id = sale_id.id

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

    def action_reset_draft(self):
        self.state = 'draft'

    @api.depends('enquiry_line_ids.price_subtotal')
    def _amount_total(self):
        for amount in self:
            amount_total = 0.0
            for line in amount.enquiry_line_ids:
                amount_total += line.price_subtotal
            amount.update({
                'amount_total': amount_total,
            })


class SalesEnquiryLine(models.Model):
    _name = 'sales.enquiry.lines'
    _description = "Sales Enquiry Line Details"

    enquiry_lines = fields.Many2one('sales.enquiry', ondelete='cascade', string="SalesEnquiry", required=True)
    product_id = fields.Many2one('product.product', string='Product')
    description = fields.Text(string='Description')
    quantity = fields.Float(string="Quantity ", default=1.0)
    product_uom = fields.Many2one('uom.uom', 'Unit of Measure')
    price_unit = fields.Float(String='Unit Price', digits='Product Price', default=0.0)
    price_subtotal = fields.Float(compute='_compute_total', string='Subtotal', store=True)

    @api.depends('quantity', 'price_unit', 'price_subtotal')
    def _compute_total(self):
        for order in self:
            price_subtotal = 0.0
            for line in order:
                price_subtotal = line.quantity * line.price_unit
            line.price_subtotal = price_subtotal

    @api.onchange('product_id')
    def product_id_change(self):
        if self.product_id:
            self.price_unit = self.product_id.list_price or 0


class Salesorder(models.Model):
    _inherit = 'sale.order'
    _description = "Sales Inherited"

    discount = fields.Float(String='Discount')

    def button_updates(self):
        for line in self.order_line:
            line.discount = self.discount

    def _prepare_invoice(self):
        invoice_vals = super(Salesorder, self)._prepare_invoice()
        invoice_vals['discount'] = self.discount
        return invoice_vals
