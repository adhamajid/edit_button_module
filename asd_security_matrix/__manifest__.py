# -*- coding: utf-8 -*-
{
    'name': "asd_security_matrix",

    'summary': """Security matrix for MG""",

    'description': """
        Security matrix for MG
    """,

    'author': "PT. Arkana Solusi Digital",
    'website': "http://www.arkana.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'base_user_role',
        'account',
        'payment',
        'dh_incentive',
        'dh_payment',
        ],

    # always loaded
    'data': [
        'security/account_security.xml',
        'security/security.xml',
        'security/menus.xml',
        # 'security/ir.model.access.csv',
        'views/account_editbutton.xml',
        'views/account_move_views.xml',
        'views/account_payment_views.xml',
        'views/cash_advance_views.xml',
        'views/cash_settlement_views.xml',
        'views/complimentary_views.xml',
        'views/voucher_views.xml',
    ],
    # only loaded in demonstration mode

    "test": [],
    "js": [],
    "css": [],
    "qweb": [],
}
