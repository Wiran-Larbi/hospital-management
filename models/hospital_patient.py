from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    contact = fields.Char(string='Contact Number')
    
    # Stored computed field for the count of appointments
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count', store=True)

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_ids)

    # Assuming you have a one2many relation from patients to appointments
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')
    @api.model
    def create(self, vals):
        
        patient_record = super(HospitalPatient, self).create(vals)

        user_vals = {
            'name': patient_record.name,
            'login': patient_record.name.replace(" ", "_").lower(),  
            'password': patient_record.name.replace(" ", "_").lower(),
            'groups_id': [(4, self.env.ref('hospital-management.group_hospital_patient').id)]
        }
        # Creation of the patient
        try:
            self.env['res.users'].sudo().create(user_vals)
        except Exception as e:
            raise ValidationError("Error creating user: %s" % e)

        return patient_record
