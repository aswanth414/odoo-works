# -*- coding: utf-8 -*-
{
    'name': "Open Academycourses",
    'summary': """Manage trainings""",
    'description': """
    Open Academy module for managing trainings:
    - training courses
    - training sessions
    - attendees registration
""",
    'author': "My Company",
    'website': "http://www.openacademy.com",
    'category': 'Test',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/sessions.xml',
    ],
    'demo': [],
}
