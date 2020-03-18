# -*- coding: utf-8 -*-

from odoo import models, fields, api

class o3_admission(models.Model):
    _inherit = "op.admission"

    x_grade_applied = fields.Char("Grade Applied", size=64)
    x_grade_eligible = fields.Char("Grade Eligible", size=64)
    x_student_in_qatar = fields.Selection([('yes', 'Y'), ('no', 'N')], "Student Already Arrived")
    x_expected_date_arrival = fields.Date("Date of Arrival")
