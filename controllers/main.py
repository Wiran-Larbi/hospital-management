from odoo import http
from odoo.http import request

class HospitalController(http.Controller):

    @http.route('/hospital/patients', auth='public')
    def list_patients(self, **kwargs):
        patients = request.env['hospital.patient'].search([])
        return request.render('gestion_hospitaliere.list_patients_template', {
            'patients': patients
        })

    @http.route('/hospital/doctors', auth='public')
    def list_doctors(self, **kwargs):
        doctors = request.env['hospital.doctor'].search([])
        return request.render('gestion_hospitaliere.list_doctors_template', {
            'doctors': doctors
        })
