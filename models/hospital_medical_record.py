from odoo import models, fields

class HospitalMedicalRecord(models.Model):
    _name = 'hospital.medical_record'
    _description = 'Hospital Medical Record'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    date = fields.Date(string='Date of Record')
    diagnosis = fields.Text(string='Diagnosis')
    prescription = fields.Text(string='Prescription')