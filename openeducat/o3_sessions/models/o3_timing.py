from odoo import models, fields

class o3_sessions(models.Model):
    _inherit = ["op.timing"]
    minute = fields.Selection([('00', '00'), ('05', '05'), ('10', '10'), ('15','15'), ('20', '20'), ('25', '25'),
                               ('30','30'), ('35', '35'), ('40', '40'), ('45', '45'), ('50', '50'), ('55', '55')])


