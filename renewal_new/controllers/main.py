from odoo import http
from datetime import datetime as dt
from odoo.http import request
from werkzeug.utils import redirect


class Period(http.Controller):

    @http.route('/update/records', auth='public', type='http', website=False)
    def submit_request(self, **kw):
        subitems = request.env['domain.inherit'].sudo().search([])
        # print("subitems: ", subitems)
        start_date = kw.get('start_date')
        end_date = kw.get('end_date')

        if start_date and end_date:
            init_date = dt.strptime(str(start_date), '%Y-%m-%d').date()                     # converting datetime object to date object
            final_date = dt.strptime(str(end_date), '%Y-%m-%d').date()
            for i in subitems:
                sum_line_invoice_amount = 0
                sum_bill_line_purchase_amount = 0
                quantity = 0
                bill_quantity = 0
                move_line_ids = request.env['account.move.line'].search([('move_id.type', '=', 'out_invoice'), ('domain_ids', '=', i.id), ('move_id.state', '!=', 'cancel')])
                # print(f'move_line_ids of {i.domain_ids} is {move_line_ids}')
                bill_move_line_ids = request.env['account.move.line'].search([('move_id.type', '=', 'in_invoice'), ('domain_ids', '=', i.id), ('move_id.state', '!=', 'cancel')])
                if move_line_ids:
                    # print("\nINVOICE RECORDS.....................")
                    for line in move_line_ids:
                        if line.start_date and line.end_date:
                            if line.end_date > init_date or line.end_date == init_date:                                         # filtering move_lines based on the dates given
                                if (line.start_date < init_date or line.start_date == init_date):
                                    # print(f'LESSER line.start_date: {line.start_date}, Given start_date: {init_date}')
                                    starting = dt.strptime(str(start_date), '%Y-%m-%d')
                                else:
                                    # print(f'GREATER line.start_date: {line.start_date}, Given start_date: {init_date}')
                                    starting = dt.strptime(str(line.start_date), '%Y-%m-%d')
                                if line.end_date > final_date or line.end_date == final_date:
                                    # print(f'GREATER line.end_date: {line.end_date}, Given end_date: {final_date}')
                                    ending = dt.strptime(str(end_date), '%Y-%m-%d')
                                else:
                                    # print(f'LESSER line.end_date: {line.end_date}, Given end_date: {end_date}')
                                    ending = dt.strptime(str(line.end_date), '%Y-%m-%d')
                                duration_days = float(str((ending - starting).days))                                            # got duration_days
                                # print(f'Duration days of line: {line} of move {line.move_id.name}:  {duration_days}')
                                sum_line_invoice_amount = sum_line_invoice_amount + (duration_days * line.one_day_cost)         # calculating the Invoice Amount
                                quantity = quantity + line.quantity                                                             # calculating the Invoice Quantity

                    i.invoice_amount = sum_line_invoice_amount
                    i.invoice_quantity = quantity

                if bill_move_line_ids:
                    # print("\nBILL RECORDS.....................")
                    for bill_line in bill_move_line_ids:
                        if bill_line.start_date and bill_line.end_date:
                            if bill_line.end_date > init_date or bill_line.end_date == init_date:               # filtering bill_lines based on the dates given
                                if bill_line.start_date < init_date or bill_line.start_date == init_date:
                                    # print(f'LESSER bill line.start_date: {bill_line.start_date}, Given start_date: {init_date}')
                                    starting = dt.strptime(str(start_date), '%Y-%m-%d')
                                else:
                                    # print(f'GREATER bill line.start_date: {bill_line.start_date}, Given start_date: {init_date}')
                                    starting = dt.strptime(str(bill_line.start_date), '%Y-%m-%d')
                                if bill_line.end_date > final_date or bill_line.end_date == final_date:
                                    # print(f'GREATER bill line.end_date: {bill_line.end_date}, Given end_date: {final_date}')
                                    ending = dt.strptime(str(end_date), '%Y-%m-%d')
                                else:
                                    # print(f'LESSER bill line.end_date: {bill_line.end_date}, Given end_date: {end_date} or {final_date}')
                                    ending = dt.strptime(str(bill_line.end_date), '%Y-%m-%d')
                                duration_days = float(str((ending - starting).days))                            # got duration_days
                                # print(f'Duration days of bill line: {bill_line} of move {bill_line.move_id.name}:  {duration_days}')
                                sum_bill_line_purchase_amount = sum_bill_line_purchase_amount + (duration_days * bill_line.one_day_cost)                            # calculating the Purchase Amount
                                bill_quantity = bill_quantity + bill_line.quantity                                                                                  # calculating the Purchase Quantity
                    i.purchase_amount = sum_bill_line_purchase_amount
                    i.purchase_quantity = bill_quantity
            return redirect('/web#action=renewal_new.subscription_subitems_action')

        elif not start_date or not end_date:
            return redirect('/web#action=renewal_new.subscription_subitems_action')



