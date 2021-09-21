# -*- coding: utf-8 -*-
{
    'name': "Invoice_Email_remainder",

    'summary': """Email Reminder""",

    'description': """Email Reminder for account module """,

    'author': "Aswanth J V",
    'website': "",

    'category': 'Test',
    'version': '0.1',

    'depends': ['account', 'mail'],

    'data': [
        'views/remainder.xml',
        'security/ir.model.access.csv',
        'data/email_template.xml',
        'data/email_ir_cron.xml',
    ],
}
