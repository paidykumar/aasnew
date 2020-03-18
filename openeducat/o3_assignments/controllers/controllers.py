# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.tools import groupby as groupbyelem

from odoo.osv.expression import OR


class AssignmentsReport(http.Controller):
    @http.route('/assignment/submit', type='http', auth='public', website=True)
    def portal_student_submit_assignment_data(self, **kw):
        student_ids = request.env['op.assignment.sub.line'].sudo().search([('user_id', '=', request.session.uid)])
        return request.render("o3_assignments.portal_student_submit_assignment_data", {'student_ids': student_ids})

    @http.route('/submited/assignment/list', type='http', auth='public', website=True)
    def assignment_data(self, **kw):
        student_ids = request.env['op.assignment.sub.line'].sudo().search([('user_id', '=', request.session.uid)])
        return request.render("o3_assignments.assignment_data", {'student_ids': student_ids})

