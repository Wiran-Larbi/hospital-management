from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Name', required=True)
    specialization = fields.Char(string='Specialization')
    contact = fields.Char(string='Contact Number')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count', store=True)

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_ids)

    appointment_ids = fields.One2many('hospital.appointment', 'doctor_id', string='Appointments')
    @api.model
    def create(self, vals):
        
        doctor_record = super(HospitalDoctor, self).create(vals)

        user_vals = {
            'name': doctor_record.name,
            'login': doctor_record.name.replace(" ", "_").lower(),  
            'password': doctor_record.name.replace(" ", "_").lower(),
            'groups_id': [(4, self.env.ref('hospital-management.group_hospital_doctor').id)]
        }

        try:
            self.env['res.users'].sudo().create(user_vals)
        except Exception as e:
            raise ValidationError("Error creating user: %s" % e)

        return doctor_record
