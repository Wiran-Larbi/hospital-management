from odoo import api, models, fields

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Information'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    contact = fields.Char(string='Contact Information')
    address = fields.Text(string='Address')
    medical_history = fields.Text(string='Medical History')
    # Add more fields as needed

    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')
    medical_record_ids = fields.One2many('hospital.medical.record', 'patient_id', string='Medical Records')
    doctor_ids = fields.Many2many('hospital.doctor', string='Doctors')