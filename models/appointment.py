from odoo import api, models, fields

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment Information'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    date_time = fields.Datetime(string='Date & Time', required=True)
    reason = fields.Text(string='Reason for Appointment')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')
    # Add more fields as needed

    doctor = fields.Many2one('hospital.doctor', related='doctor_id', string='Doctor', store=True)
    patient = fields.Many2one('hospital.patient', related='patient_id', string='Patient', store=True)