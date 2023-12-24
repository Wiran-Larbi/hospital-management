from odoo import http
from odoo.http import request

class HospitalController(http.Controller):

    @http.route('/hospital/patients', auth='public')
    def list_patients(self, **kwargs):
        patients = request.env['hospital.patient'].search([])
        return request.render('gestion_hospitaliere.list_patients', {
            'patients': patients
        })

    @http.route('/hospital/doctors', auth='public')
    def list_doctors(self, **kwargs):
        doctors = request.env['hospital.doctor'].search([])
        return request.render('gestion_hospitaliere.list_doctors', {
            'doctors': doctors
        })
    
    @http.route('/hospital/login', type='http', auth="public", website=True)
    def hospital_login(self, **kwargs):
        return request.render("gestion_hospitaliere.hospital_login", {})

    @http.route('/hospital/login/authenticate', type='http', auth="none", methods=['POST'], website=True)
    def hospital_authenticate(self, **post):
        uid = request.session.authenticate(request.session.db, post['login'], post['password'])
        if uid:
            return http.redirect_with_hash('/hospital/patients')  # Redirect to a specific page after login
        else:
            return request.render("gestion_hospitaliere.hospital_login", {'error': "Invalid credentials"})
