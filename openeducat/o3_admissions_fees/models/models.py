# -*- coding: utf-8 -*-

from odoo import models, fields, api

class o3_admissions_fees(models.Model):
    _inherit = 'op.admission'

    fees = fields.Float('Fees', states={'done': [('readonly', True)]}, compute='set_fees')


    @api.depends('fees_term_id', 'register_id')
    def set_fees(self):
        for obj in self.fees_term_id:
            if obj.name[-2:] == '01':
                self.fees = self.register_id.product_id.lst_price * 1
            elif obj.name[-2:] == '02':
                self.fees = self.register_id.product_id.lst_price * 2
            elif obj.name[-2:] == '03':
                self.fees = self.register_id.product_id.lst_price * 3
            elif obj.name[-2:] == '04':
                self.fees = self.register_id.product_id.lst_price * 4
            elif obj.name[-2:] == '05':
                self.fees = self.register_id.product_id.lst_price * 5
            elif obj.name[-2:] == '06':
                self.fees = self.register_id.product_id.lst_price * 6
            elif obj.name[-2:] == '07':
                self.fees = self.register_id.product_id.lst_price * 7
            elif obj.name[-2:] == '08':
                self.fees = self.register_id.product_id.lst_price * 8
            else:
                self.fees = self.register_id.product_id.lst_price



class o3_admissions_fees_termsline(models.Model):
    _inherit = 'op.fees.terms.line'

    value = fields.Float('Value (%)', digits=(16, 6))
