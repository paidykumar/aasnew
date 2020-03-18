# -*- coding: utf-8 -*-

from odoo import models, fields, api

class assignments_report(models.Model):
    code = fields.Char('Code', size=16, required=True)
#     _name = 'o3_assignments_report.o3_assignments_report'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100