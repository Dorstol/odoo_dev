from odoo import models, fields


class Diagnosis(models.Model):
    _name = "hr.diagnosis"
    _description = "Diagnosis Information"

    visit_id = fields.Many2one(
        "hr.patient.visit",
        required=True,
    )
    diagnose = fields.Char(
        required=True,
    )
    description = fields.Text()
    approved = fields.Boolean(
        default=False,
    )
