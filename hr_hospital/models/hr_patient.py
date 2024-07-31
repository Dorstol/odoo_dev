from odoo import models, fields, api
from datetime import date


class Patient(models.Model):
    _inherit = "hr.person"
    _name = "hr.patient"
    _description = "Patient"

    personal_doctor = fields.Many2one(
        "hr.doctor",
        required=True,
    )
    date_of_birth = fields.Date(
        required=True,
    )
    passport_data = fields.Char(
        required=True,
    )
    contact_person = fields.Char()
    age = fields.Integer(
        compute="_compute_age",
        store=True,
    )
    disease_ids = fields.Many2many(
        "hr.disease",
    )
    doctor_id = fields.Many2one(
        "hr.doctor",
    )
    visit_ids = fields.One2many(
        "hr.patient.visit",
        "patient_id",
    )

    @api.depends("date_of_birth")
    def _compute_age(self):
        today = date.today()

        for record in self:
            if record.date_of_birth:
                birth_date = record.date_of_birth
                record.age = (
                    today.year
                    - birth_date.year
                    - ((today.month, today.day) < (birth_date.month, birth_date.day))
                )
            else:
                record.age = 0
