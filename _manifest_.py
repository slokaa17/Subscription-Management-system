{
    'name': 'Subscription Management System',

    'version': '18.0.1.0.0',

    'summary': 'Manage subscriptions, plans, invoices and payments',

    'description': """
        Subscription Management System
        Developed for Brightloop Software.

        Features:
        - Product Management
        - Subscription Plans
        - Subscription Management
        - Invoice Management
        - Discount Management
        - Payment Management
        - Dashboard
    """,

    'category': 'Services',

    'author': 'Your Team',

    'license': 'LGPL-3',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
    'views/product_views.xml',
    ],

    'installable': True,

    'application': True,
}