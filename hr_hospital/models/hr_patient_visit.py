from odoo import models, fields


class PatientVisit(models.Model):
    _name = "hr.patient.visit"
    _description = "Visit"

    visit_status = fields.Selection(
        [("planned", "Planned"), ("completed", "Completed"), ("canceled", "Canceled")],
        required=True,
    )
    planned_date = fields.Datetime(
        default=lambda self: fields.Datetime.now(),
    )
    doctor_id = fields.Many2one(
        "hr.doctor",
    )
    patient_id = fields.Many2one(
        "hr.patient",
    )
    notes = fields.Text()
