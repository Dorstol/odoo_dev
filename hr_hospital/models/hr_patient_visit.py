from odoo import models, fields, api, exceptions


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
    actual_date = fields.Date(
        compute="_compute_actual_date",
        store=True,
    )
    doctor_id = fields.Many2one(
        "hr.doctor",
    )
    doctor_name = fields.Char(
        related="doctor_id.full_name",
        store=True,
    )
    patient_id = fields.Many2one(
        "hr.patient",
    )
    patient_name = fields.Char(
        related="patient_id.patient_name",
        store=True,
    )
    diagnosis_ids = fields.One2many(
        "hr.diagnosis",
        "visit_id",
    )
    notes = fields.Text()

    @api.depends("planned_date")
    def _compute_actual_date(self):
        for record in self:
            if record.planned_date:
                record.actual_date = record.planned_date.date()
            else:
                record.actual_date = None

    @api.constrains("visit_status", "planned_date", "actual_date", "doctor_id", "patient_id")
    def _check_visit_constraints(self):
        for record in self:
            if record.visit_status == "completed":
                if record.planned_date != record.actual_date:
                    raise exceptions.ValidationError(
                        "Can`t change time, date and doctor for completed visit."
                    )

    @api.constrains("diagnosis_ids")
    def _check_deletion_and_archiving(self):
        if self.diagnosis_ids:
            raise exceptions.ValidationError(
                "Can`t delete or archive visits with diagnosis."
            )

    @api.constrains('patient_id', 'doctor_id', 'planned_date')
    def _check_unique_visit(self):
        for record in self:
            existing_visits = self.search([
                ('patient_id', '=', record.patient_id.id),
                ('doctor_id', '=', record.doctor_id.id),
                ('planned_date', '>=', fields.Date.to_string(record.planned_date.date()) + ' 00:00:00'),
                ('planned_date', '<=', fields.Date.to_string(record.planned_date.date()) + ' 23:59:59'),
                ('id', '!=', record.id),
            ])
            if existing_visits:
                raise exceptions.ValidationError(
                    "A patient may not be registered with one doctor more than once a day."
                )
