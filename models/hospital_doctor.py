from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Name', required=True)
    specialization = fields.Char(string='Specialization')
    contact = fields.Char(string='Contact Number')
    
    @api.model
    def create(self, vals):
        # Create the doctor record
        doctor_record = super(HospitalDoctor, self).create(vals)

        # Prepare user values
        user_vals = {
            'name': doctor_record.name,
            'login': doctor_record.name.replace(" ", "_").lower(),  # Creating login from the name
            'password': doctor_record.name.replace(" ", "_").lower(),
            'groups_id': [(4, self.env.ref('hospital-management.group_doctor').id)]
        }

        # Create the user
        try:
            self.env['res.users'].sudo().create(user_vals)
        except Exception as e:
            raise ValidationError("Error creating user: %s" % e)

        return doctor_record
