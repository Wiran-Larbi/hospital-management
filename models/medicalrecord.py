from odoo import api, models, fields

class MedicalRecord(models.Model):
    _name = 'hospital.medical.record'
    _description = 'Patient Medical Record'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    date = fields.Date(string='Record Date', default=fields.Date.today())
    diagnosis = fields.Text(string='Diagnosis')
    prescription = fields.Text(string='Prescription')
    # Add more fields for test results, treatment plans, etc.
