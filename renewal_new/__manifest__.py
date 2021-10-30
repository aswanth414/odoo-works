# -*- coding: utf-8 -*-
{
    'name': "Subscription",

    'summary': """Renewal/Subscription Reports""",

    'description': """Renewal Reports for account module """,

    'author': "",
    'website': "",

    'category': 'Test',
    'version': '0.1',

    'depends': ['web', 'base', 'account', 'product', 'febno_domain_buy', 'account_subitems_update_search', 'account_subitems'],

    'data': [
        'data/data.xml',
        'data/groups.xml',
        'wizards/wizzard_report.xml',
        'views/templates.xml',
        'views/renewal.xml',
        'views/end_customer_search.xml',
        'views/account_move_view.xml',
        'views/sale_order_form.xml',
        'views/subitems.xml',
        'reports/report_template.xml',
        'reports/reports.xml',

    ],
    'qweb': [
        "static/src/xml/base.xml",
    ],
    'bootstrap': True,
}
