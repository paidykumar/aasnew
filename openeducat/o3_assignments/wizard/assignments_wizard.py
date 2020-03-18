# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from datetime import datetime
from datetime import timedelta

from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

from odoo import models, fields, api, _


class SessionReport(models.TransientModel):
    _name = "o3.assignments.report"
    _description = "Grading Summary Report"

    semester = fields.Selection(
        [('s1', 'S1'), ('s2', 'S2'), ('all', 'ALL')],
        string='Select', required=True, default='s1')
    course_id = fields.Many2one('op.course', 'Course')
    batch_id = fields.Many2one('op.batch', 'Batch')
    # assignment_id = fields.Many2one('op.assignment', 'Assignment')
    subject_id = fields.Many2one('op.subject', 'Subject')
    # faculty_id = fields.Many2one('op.faculty', 'Faculty')
    # start_date = fields.Date(
    #     'Start Date', required=True,
    #     default=(datetime.today() - relativedelta(
    #         days=datetime.date(
    #             datetime.today()).weekday())).strftime('%Y-%m-%d'))
    # end_date = fields.Date(
    #     'End Date', required=True,
    #     default=(datetime.today() + relativedelta(days=366 - datetime.date(
    #         datetime.today()).weekday())).strftime('%Y-%m-%d'))

    @api.multi
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for session in self:
            start_date = fields.Date.from_string(session.start_date)
            end_date = fields.Date.from_string(session.end_date)
            if end_date < start_date:
                raise ValidationError(_('End Date cannot be set before \
                Start Date.'))
            elif end_date > (start_date + timedelta(days=366)):
                raise ValidationError(_("Select date range for a year!"))

    @api.onchange('course_id')
    def onchange_course(self):
        if self.batch_id and self.course_id:
            if self.batch_id.course_id != self.course_id:
                self.batch_id = False

    @api.multi
    def gen_grading_summary_report(self):
        data = self.read(
            ['semester', 'course_id', 'batch_id', 'subject_id'])[0]
        assignment_ids = self.env['op.assignment'].search(
                [('subject_id', '=', data['subject_id'][0]),
                 ('course_id', '=', data['course_id'][0]),
                 ('batch_id', '=', data['batch_id'][0])])
        data.update({'assignment_ids': assignment_ids.ids})
        template = self.env.ref(
                'o3_assignments.report_assignments_marksheet')

        return template.report_action(self, data=data)
