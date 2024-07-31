from odoo import models, fields


class Person(models.AbstractModel):
    _name = "hr.person"
    _description = "Abstract model for person"

    first_name = fields.Char(
        required=True,
    )
    second_name = fields.Char(
        required=True,
    )
    phone_number = fields.Char(
        required=True,
    )
    photo = fields.Image()
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")],
        required=True,
        default="male",
    )
