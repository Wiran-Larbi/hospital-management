from odoo import models, fields

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'

    name = fields.Char(string="Appointment ID", readonly=True, copy=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    date_time = fields.Datetime(string='Date and Time', required=True)
    date_start = fields.Datetime()
    reason = fields.Text(string='Reason for Appointment')
    status = fields.Selection([('scheduled', 'Scheduled'),('completed', 'Completed'),('cancelled', 'Cancelled')],default='scheduled', string='Status')
    
    def print_prescription(self):
        return self.env.ref('hospital-management.report_print_prescription').report_action(self)


    ##def schedule(self):
    ##    self.ensure_one()
	##	self.status = 'scheduled'

    ##def complete(self):
    ##    self.ensure_one()
	##	self.status = 'completed'

    ##def cancel(self):
    ##    self.ensure_one()
	##	self.status = 'cancelled'

    ##def print_prescription(self):
	##	return self.env.ref('hospital-management.report_print_prescription').report_action(self)
    
    ##@api.model
    ##def create(self, vals):
    ##    vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or 'APPOINTMENT'
    ##    msg_body = 'Appointment created'
    ##    for msg in self:
    ##        msg.message_post(body=msg_body)
    ##    result = super(HospitalAppointment, self).create(vals)
    ##    return result