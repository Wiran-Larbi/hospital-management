{
    'name': 'Gestion Hospitalière',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Hospital Management System for Odoo',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/record_rules.xml', 
        'security/ir.model.access.csv',
        'views/menu.xml',  # Menu items
        'views/hospital_patient_views.xml',  # Views for different models
        'views/hospital_doctor_views.xml',
        'views/hospital_appointment_views.xml',
        'views/hospital_medical_record_views.xml',
        'views/hospital_appointment_kanban_view.xml',  # Kanban view for appointments
        'views/hospital_login.xml'
    ],
    'demo': ['demo/demo.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}