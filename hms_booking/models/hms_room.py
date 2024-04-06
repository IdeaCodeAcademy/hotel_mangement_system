from odoo import api, fields, models

class HmsRoom(models.Model):
    _name = "hms.room"
    _description = "HMS Room"

    name = fields.Char(string="Room Name")
    hms_floor_id = fields.Many2one("hms.floor", string="Floor")
