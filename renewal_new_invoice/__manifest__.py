# -*- coding: utf-8 -*-
{
    'name': "Reminder",

    'summary': """Email Reminder""",

    'description': """Email Reminder for account module """,

    'author': "",
    'website': "",

    'category': 'Test',
    'version': '0.1',

    'depends': ['account', 'mail'],

    'data': [
        'data/mail_template.xml',
        'data/reminder_cron.xml',
        'data/group.xml',
        'views/reminder.xml',
        'security/ir.model.access.csv',

    ],
}
