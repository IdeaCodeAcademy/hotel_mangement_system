from odoo import api, fields, models

class HmsFloor(models.Model):
    _name = 'hms.floor'
    _description = 'HmsFloor'

    name = fields.Char()