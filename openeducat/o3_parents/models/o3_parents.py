# -*- coding: utf-8 -*-

from odoo import models, fields, api

class o3_parents(models.Model):
    _inherit = 'op.parent'

    x_workplace_father = fields.Char("Workplace", size=64)
    x_job_position_father = fields.Char("Job Position", size=64)
    x_passport_number_father = fields.Char("Passport Number", size=64)
    x_qatar_id_number_father = fields.Char("ID Number", size=64)
    x_mobile_mother = fields.Char("Mother Mobile", size=64)
    x_name_mother = fields.Char("Mother Name", size=64)
