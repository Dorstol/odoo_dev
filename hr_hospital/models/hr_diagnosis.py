from odoo import models, fields


class Diagnosis(models.Model):
    _name = "hr.diagnosis"
    _description = "Diagnosis Information"

    visit_id = fields.Many2one(
        "hr.patient.visit",
        required=True,
    )
    disease_id = fields.Many2one(
        "hr.disease",
        required=True,
    )
    disease_name = fields.Char(
        related="disease_id.name",
        store=True,
    )
    description = fields.Text()
    approved = fields.Boolean(
        default=False,
    )
