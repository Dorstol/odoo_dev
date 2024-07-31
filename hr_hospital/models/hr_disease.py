from odoo import models, fields


class Disease(models.Model):
    _name = "hr.disease"
    _description = "Disease"

    name = fields.Char(
        required=True,
    )
    description = fields.Text()
