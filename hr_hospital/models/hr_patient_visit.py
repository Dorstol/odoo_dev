from odoo import models, fields


class PatientVisit(models.Model):
    _name = 'hr.patient.visit'
    _description = 'Visit'

    date = fields.Date(required=True)
    doctor_id = fields.Many2one('hr.doctor')
    patient_id = fields.Many2one('hr.patient')
    notes = fields.Text()
