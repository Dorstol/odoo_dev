# -*- coding: utf-8 -*-
{
    'name': 'www-site',
    'version': '17.0.0.0.1',
    'category': 'Website',
    'summary': 'Educational module for Odoo website development',
    'description': """
        This module serves as an educational example for developing websites in Odoo.
    """,
    'author': 'Sofronov Oleh',
    'website': 'https://github.com/Dorstol',
    'depends': ['base',],
    'data': [
        # Add XML or CSV files here that contain data to be loaded when the module is installed
        # Example:
        # 'data/my_data.xml',
    ],
    'demo': [
        # Add demo XML or CSV files here that provide some demo data (optional)
        # Example:
        # 'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',

    'iamges': [
        'static/description/icon.png',
    ],

    'price': 0,
    'currency': 'EUR',
}
