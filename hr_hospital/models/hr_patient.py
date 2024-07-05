from odoo import models, fields


class Patient(models.Model):
    _name = 'hr.patient'
    _description = 'Patient'

    full_name = fields.Char(required=True)
    age = fields.Integer(required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True, default='male')
    disease_ids = fields.Many2many('hr.disease')
    doctor_id = fields.Many2one('hr.doctor')
    visit_ids = fields.One2many('hr.patient.visit', 'patient_id')
