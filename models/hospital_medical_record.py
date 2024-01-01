from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalMedicalRecord(models.Model):
    _name = 'hospital.medical_record'
    _description = 'Hospital Medical Record'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    date = fields.Date(string='Date of Record')
    diagnosis = fields.Text(string='Diagnosis')
    prescription = fields.Text(string='Prescription')
    
    
    def print_prescription(self):
        for record in self:
            self.ensure_one()
            return self.env.ref('hospital-management.medical_record_pdf_report').report_action(self)