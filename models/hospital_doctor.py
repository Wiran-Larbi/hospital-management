from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Name', required=True)
    specialization = fields.Char(string='Specialization')
    contact = fields.Char(string='Contact Number')
