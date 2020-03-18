# -*- coding: utf-8 -*-
from collections import OrderedDict
from operator import itemgetter

from odoo import http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.tools import groupby as groupbyelem

from odoo.osv.expression import OR


class O3StudentInformation(http.Controller):

    # def _prepare_portal_layout_values(self):
    #     values = super(CustomerPortal, self)._prepare_portal_layout_values()
    #     return values

    @http.route('/student/profile', type='http', auth='public', website=True)
    def openeducat_enterprise_student_portal(self, **kw):
        student = request.env['op.student'].sudo().search([('user_id', '=', request.session.uid)])
        return request.render("o3_student.openeducat_enterprise_student_portal", {'student': student})



