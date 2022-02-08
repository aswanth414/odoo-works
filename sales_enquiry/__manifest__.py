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
    'depends': ['base', 'sale', 'account'],
    'data': [
        'sales_views/sales_views.xml',
        'sales_views/sales_inherit_views.xml',
        'sales_views/invoice_inherit.xml',
        'data/sales_enq_sequ.xml',
        'security/ir.model.access.csv',
        'wizard/sales_confirm_enquiry.xml',
        'report/sales_enquiry_report.xml',
        'report/report_sales_enquiry_template.xml',
    ],
    'demo': [],
}
