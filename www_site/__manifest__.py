# -*- coding: utf-8 -*-
{
    'name': 'www-site',
    'version': '17.0.0.0.1',
    'category': 'Website',
    'summary': 'Educational module for Odoo website development',
    'author': 'Sofronov Oleh',
    'website': 'https://github.com/Dorstol',
    'depends': ['base', ],
    'data': [
        'security/ir.model.access.csv',
        'views/www_site_view.xml',
    ],
    'demo': [
        'demo/www_site_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',

    'images': [
        'static/description/icon.png',
    ],

    'price': 0,
    'currency': 'EUR',
}
