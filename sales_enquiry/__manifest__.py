# -*- coding: utf-8 -*-
{
    'name': "Sales Enquiry",
    'summary': """Manage Sales Enquiry Details""",
    'description': """
    Sales Enquiry module for managing sales enquiry details:
    - Sales Enquiry 
    - Sales Enquiry Customer
""",
    'author': "Sales Company",
    'website': "http://www.sales_enquiry.com",
    'category': 'Test',
    'version': '0.1',
    'depends': ['base', 'sale'],
    'data': [
        'sales_views/sales_views.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
}
