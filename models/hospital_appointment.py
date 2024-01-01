from odoo import models, fields

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    doctor_specialization = fields.Char(related='doctor_id.specialization', string='Doctor Specialization', store=True, readonly=True)
    date_time = fields.Datetime(string='Date and Time', required=True)
    reason = fields.Text(string='Reason for Appointment')
    status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], default='scheduled', string='Status')
