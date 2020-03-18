# -*- coding: utf-8 -*-
from odoo import models, fields, api

class o3_library(models.Model):
    _inherit = 'op.media'

    series = fields.Char('Series', size=64)
    classification = fields.Char('Classification', size=64)
    language = fields.Selection(
        [('english', 'English'), ('french', 'French'), ('arabic', 'Arabic')],
        'Language', default='english')
    tags = fields.Many2many('op.tag', string='Keyword(s)')



class o3Publisher(models.Model):
    _inherit = "op.publisher"

    name = fields.Char('Name', size=50, required=True)







