{
    'name': 'Hospital Management',
    'version': '17.0.0.0.1',
    'summary': 'Module for managing hospital records.',
    'sequence': -100,
    'category': 'Healthcare',
    'website': 'https://github.com/Dorstol/odoo_dev',
    'author': 'Sofronov Oleh',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_doctor_view.xml',
        'views/hr_patient_view.xml',
        'views/hr_disease_view.xml',
        'views/hr_patient_visit_view.xml',
        'views/hr_hospital_menu.xml',
    ],
    'demo': [
        'demo/doctor_demo.xml',
        'demo/patient_demo.xml',
    ],

    'images': [
        'static/description/icon.png',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
