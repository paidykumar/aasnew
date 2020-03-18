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

import time
from odoo import models, api, fields


class ReportProgressReport(models.AbstractModel):
    _name = "report.o3_spr.student_progress_report"

    def get_objects(self, docs):
        exams = self.env['op.assignment.sub.line'].search([], order='student_id desc')
        data_list = []
        for assignment_obj in exams:
            if docs.batch_id == assignment_obj.assignment_id.batch_id:
                assignment_data = {
                    'student': assignment_obj.student_id.name + " " + assignment_obj.student_id.middle_name + " " +
                               assignment_obj.student_id.last_name,
                    'subject': assignment_obj.assignment_id.subject_id.name,
                    'course': assignment_obj.assignment_id.course_id.name,
                    'batch': assignment_obj.assignment_id.batch_id.name,
                    'faculty_id': assignment_obj.assignment_id.faculty_id.name,
                    'school_year': str(assignment_obj.assignment_id.batch_id.start_date.strftime(
                        '%Y') + " - " + assignment_obj.assignment_id.batch_id.end_date.strftime('%Y')),
                    'assignment_code': assignment_obj.assignment_id.assignment_type_id.code,
                    'marks': assignment_obj.marks,

                }
                data_list.append(assignment_data)
            final_list = self.sort_tt(data_list)

        return final_list


    def sort_tt(self, data_list):
        main_list = []
        f = []
        for d in data_list:
            if d['student'] not in f:
                f.append(d['student'])
                main_list.append({
                    'student': d['student'],
                    'faculty': d['faculty_id'],
                    'batch': d['batch'],
                    'school_year': d['school_year'],
                    'line': [],
                })
                for m in main_list:
                    if m['student'] == d['student']:
                        m['line'].append({'subject': d})

            else:
                for m in main_list:
                    if m['student'] == d['student']:
                        m['line'].append({'subject': d})

        return main_list
    #this method returns assignment + main marks
    def get_marks(self,batch,student,subject):
        total_marks = 0
        marks = 0
        exam_marks = []
        obj = ['S1-CW', 'S1-HW', 'S1-PR', 'S1-UT', 'S1-QZ1', 'S1-QZ2', 'S1-QZ3']
        assignment_marks = self.env['op.assignment.sub.line'].search([], order='student_id desc')
        list = self.env['op.marksheet.line'].search([], order='student_id desc')
        for i in list:
            exam_marks.append(i.result_line)
        for assignment_obj in assignment_marks:
            if batch == assignment_obj.assignment_id.batch_id.name:
                if assignment_obj.student_id.name + " " + assignment_obj.student_id.middle_name + " " + assignment_obj.student_id.last_name == student:
                    if assignment_obj.assignment_id.subject_id.name == subject:
                        if assignment_obj.assignment_id.assignment_type_id.code in obj:
                            total_marks += assignment_obj.marks
        for result in exam_marks:
            for exam in result:
                if batch == exam.exam_id.session_id.batch_id.name:
                    if exam.student_id.name + " " + exam.student_id.middle_name + " " + exam.student_id.last_name == student:
                        if exam.exam_id.subject_id.name == subject:
                            marks += exam.marks

        return (total_marks + marks)

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['op.exam.session'].browse(docids)
        docargs = {
            'doc_model': 'op.assignment',
            'doc_ids': self.ids,
            'docs': docs,
            'get_objects': self.get_objects,
            'sort_tt': self.sort_tt,
            'get_marks': self.get_marks,
        }
        return docargs
