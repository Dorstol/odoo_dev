from odoo import models, fields, api
from datetime import date


class Person(models.AbstractModel):
    _name = "hr.person"
    _description = "Abstract model for person"

    first_name = fields.Char(
        required=True,
    )
    second_name = fields.Char(
        required=True,
    )
    phone_number = fields.Char()
    photo = fields.Image()
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")],
        required=True,
        default="male",
    )


class Patient(models.Model):
    _inherit = "hr.person"
    _name = "hr.patient"
    _description = "Patient"

    date_of_birth = fields.Date(
        required=True,
    )
    passport_data = fields.Char()
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
    doctor_name = fields.Char(
        related="doctor_id.full_name",
        store=True,
    )
    visit_ids = fields.One2many(
        "hr.patient.visit",
        "patient_id",
    )
    patient_name = fields.Char(
        compute="_compute_patient_name",
        store=True,
    )

    @api.depends("first_name", "second_name")
    def _compute_patient_name(self):
        for record in self:
            if record.first_name and record.second_name:
                record.patient_name = f"{record.first_name} {record.second_name}"
            elif record.first_name:
                record.patient_name = record.first_name
            else:
                record.patient_name = record.second_name

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
