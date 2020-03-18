# -*- coding: utf-8 -*-

from odoo import models, fields, api

class o3_student_information(models.Model):
    _inherit = "op.student"

    x_passport_number_student = fields.Char("Passport Number", size=64)
    x_id_number_student = fields.Char("ID Number", size=64)


