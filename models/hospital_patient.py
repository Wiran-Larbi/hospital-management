from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

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
    
    @api.model
    def create(self, vals):
        # Create the doctor record
        _logger.info("wa hnaaaaaaaaaaaa Creating a new patient record wa hanaaaaaaaaaaaaaa: %s", vals)
        patient_record = super(HospitalPatient, self).create(vals)

        # Prepare user values
        user_vals = {
            'name': patient_record.name,
            'login': patient_record.name.replace(" ", "_").lower(),  
            'password': patient_record.name.replace(" ", "_").lower(),
            'groups_id': [(4, self.env.ref('hospital-management.group_patient').id)]
        }

        # Create the user
        try:
            self.env['res.users'].sudo().create(user_vals)
        except Exception as e:
            raise ValidationError("Error creating user: %s" % e)

        return patient_record
