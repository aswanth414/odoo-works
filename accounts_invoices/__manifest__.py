# -*- coding: utf-8 -*-
{
    'name': "accounts_invoices",
    'summary': """Manage accounts invoices report""",
    'description': """
           Accounts invoices module for Qweb reports:
               - Manage invoice Qweb reports
               -Dowload Pdf Reports
     """,
    'author': "",
    'website': "",
    'category': 'Test',
    'version': '0.1',
    'depends': ['account', 'board'],
    'data': [
        'report/report.xml',
        'report/invoice.xml',
        'report/invoice_report_layout.xml',

    ],

}
