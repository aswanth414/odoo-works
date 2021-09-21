# -*- coding: utf-8 -*-
{
    'name': "accounts_invoices",
    'summary': """Manage trainings""",
    'description': """
           Open Academy module for managing trainings:
               - training courses
               - training sessions- attendees registration
     """,
    'author': "",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['account', 'board'],
    # always loaded
    'data': [
        'report/report.xml',
        'report/invoice.xml',
        'report/external_layout_customised.xml',

    ],

}
