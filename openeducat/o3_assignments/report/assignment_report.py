import calendar
import pytz
import time
from datetime import datetime
from odoo import models, api, _, tools, fields


class ReportAssignmentReport(models.AbstractModel):
    _name = "report.o3_assignments.report_assignment_report"

    def get_full_name(self, data):
        name = []
        for assignment_obj in self.env['op.assignment'].browse(
                data['assignment_ids'][0]):
            assignment_data = {
                'batch': assignment_obj.batch_id.name,
                'subject': assignment_obj.subject_id.name,
                'course': assignment_obj.course_id.name,
                'code': assignment_obj.assignment_type_id.code,
            }
            name.append(assignment_data)
        return name

    def get_faculty_01(self, data):
        faculty = ''
        for assignment_obj in self.env['op.assignment'].browse(
                data['assignment_ids']):
            if assignment_obj.assignment_type_id.code[:2] == 'S1':
                faculty = assignment_obj.faculty_id.name +" " + \
                                    assignment_obj.faculty_id.middle_name +" " + \
                                    assignment_obj.faculty_id.last_name
        return faculty

    def get_faculty_02(self, data):
        faculty2 = ''
        for assignment_obj in self.env['op.assignment'].browse(
                data['assignment_ids']):
            if assignment_obj.assignment_type_id.code[:2] == 'S2':
                faculty2 = assignment_obj.faculty_id.name + " " + \
                              assignment_obj.faculty_id.middle_name + " " + \
                              assignment_obj.faculty_id.last_name
        return faculty2

    def get_objects(self, data):
        models = []
        dict = {}
        for assignment_obj in self.env['op.assignment'].browse(
                data['assignment_ids']):
            for obj in assignment_obj.assignment_sub_line:
                models.append(obj)
        models = sorted(models, key=lambda r: r.student_id.name)
        for obj in models:
            marks1 = {}
            if obj.student_id.name not in dict and obj.assignment_id.assignment_type_id.code[:2] == 'S1':
                marks1[obj.assignment_id.assignment_type_id.code] = obj.marks
                dict[obj.student_id.name] = marks1
                # marks1.clear()
            if obj.student_id.name in dict and obj.assignment_id.assignment_type_id.code[:2] == 'S1':
                marks1[obj.assignment_id.assignment_type_id.code] = obj.marks
                dict[obj.student_id.name].update(marks1)
                # marks1.clear()
        return dict

    def get_object(self, data):
        model = []
        dicts = {}
        for assignment_obj in self.env['op.assignment'].browse(
                data['assignment_ids']):
            for obj in assignment_obj.assignment_sub_line:
                model.append(obj)
        model = sorted(model, key=lambda r: r.student_id.name)
        for obj in model:
            marks = {}
            if obj.student_id.name not in dicts and obj.assignment_id.assignment_type_id.code[:2] == 'S2':
                marks[obj.assignment_id.assignment_type_id.code] = obj.marks
                dicts[obj.student_id.name] = marks
                # marks.clear()
            if obj.student_id.name in dicts and obj.assignment_id.assignment_type_id.code[:2] == 'S2':
                marks[obj.assignment_id.assignment_type_id.code] = obj.marks
                dicts[obj.student_id.name].update(marks)
                # marks.clear()
        return dicts

    """def get_objects(self, records):
        obj = ['S1-CW', 'S1-HW', 'S1-PR', 'S1-UT', 'S1-QZ1', 'S1-QZ2', 'S1-QZ3']

        for object in records:

            marks = {
                'student': object.student_id.name,

                #'faculty': object.assignment_id.faculty_id.name,
                #'batch': object.assignment_id.batch_id.name,
                #'subject': object.assignment_id.subject_id.name,
                #'course': object.assignment_id.course_id.name,
                'code': object.assignment_id.assignment_type_id.code,
            }

            index = obj.index(object.assignment_id.assignment_type_id.code)
            marks[obj[index]] = object.assignment_id.assignment_type_id.code


        return marks
        """

    @api.model
    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_id'))
        docargs = {
            'doc_ids': self.ids,
            'doc_model': model,
            'docs': docs,
            'data': data,
            'time': time,
            'get_objects': self.get_objects,
            'get_object': self.get_object,
            'get_full_name': self.get_full_name,
            'get_faculty_01': self.get_faculty_01,
            'get_faculty_02': self.get_faculty_02,
        }
        return docargs
