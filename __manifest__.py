{
    'name': 'Gestion Hospitalière',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Hospital Management System for Odoo',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_patient_views.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_appointment_views.xml',
        'views/hospital_medical_record_views.xml',
        # Add other XML files if you have any
    ],
    'demo': [
        # XML files with demo data, if you have any
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
