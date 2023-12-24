{
    'name': 'Gestion Hospitalière',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Hospital Management System for Odoo',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
        'views/hospital_patient_views.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_appointment_views.xml',
        'views/hospital_medical_record_views.xml',
        'views/hospital_appointment_kanban_view.xml',
        'views/hospital_login.xml',
        
    ],
    'demo': [
        'demo/demo.xml',
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    
}
