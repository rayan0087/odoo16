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
    'depends': ['base', 'mail', 'product'],

    'sequence': -100,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'data/sequence_data.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/patient_tag_view.xml',
        'views/appointment_view.xml',
        'views/res_config_settings_views.xml',
        'views/operation_view.xml',
        'wizards/cancel_appointment.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # 'application': True
}