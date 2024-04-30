# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
        Hospital Management System""",

    'description': """
        Hospital Management System
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hospital',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'sequence': -100,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # 'application': True
}