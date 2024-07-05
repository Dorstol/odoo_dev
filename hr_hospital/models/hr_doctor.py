from odoo import models, fields


class Doctor(models.Model):
    _name = 'hr.doctor'
    _description = 'Doctor'

    full_name = fields.Char(required=True)
    specialization = fields.Char(required=True)
    patient_ids = fields.One2many('hr.patient', 'doctor_id')
