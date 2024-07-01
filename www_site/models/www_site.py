import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class WWWWSite(models.Model):
    _name = 'www.site'
    _description = 'WWW Site'

    name = fields.Char()
    active = fields.Boolean(default=True)
    date = fields.Date()
    yesterday = fields.Date()
    qty = fields.Integer()
    partner_id = fields.Many2one(comodel_name='res.partner')
    image = fields.Image()
