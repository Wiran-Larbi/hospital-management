from odoo import api, models, fields

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Information'

    name = fields.Char(string='Name', required=True)
    specialization = fields.Char(string='Specialization')
    contact = fields.Char(string='Contact Information')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    age = fields.Integer(string='Age')
    education = fields.Text(string='Education')
    experience = fields.Integer(string='Years of Experience')
    # Add more fields as needed

    patient_ids = fields.Many2many('hospital.patient', 'patient_doctor_rel', 'doctor_id', 'patient_id', string='Patients')
    appointment_ids = fields.One2many('hospital.appointment', 'doctor_id', string='Appointments')
