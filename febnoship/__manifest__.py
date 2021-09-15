# -*- coding: utf-8 -*-
{
    'name': "febnoship",
    'summary': """Manage trainings""",
    'description': """
           Open Academy module for managing trainings:
               - training courses
               - training sessions- attendees registration
     """,
     'author': "ANU VARGHESE",
     'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['sale', 'board'],
    # always loaded
    'data': [
          'security/security.xml',
           'security/ir.model.access.csv',
          'views/ship.xml',



     ],

}