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

import calendar
import pytz
import time
from datetime import datetime
from odoo import models, api, _, tools, fields


class ReportTimeTableTeacherGenerate(models.AbstractModel):
    _name = "report.o3_sessions.o3_timetable_teacher_generate"
    _description = "Timetable Teacher Report"

    @api.multi
    def _convert_to_local_timezone(self, time):
        '''
            Converts time as per local timezone.
        '''
        if time:
            timezone = pytz.timezone(self._context['tz'] or 'UTC')
            utc_in_time = pytz.UTC.localize(fields.Datetime.from_string(time))
            local_time = utc_in_time.astimezone(timezone)
            return local_time

    def get_full_name(self, data):
        faculty_name = self.env['op.faculty'].browse(data['faculty_id'][0])
        return ' '.join([faculty_name.name,
                         faculty_name.middle_name or '',
                         faculty_name.last_name])
    #here one by one individual dictionaries add to the line key
    def sort_tt(self, data_list):
        main_list = []
        f = []
        for d in data_list:

            if d['teacher'] not in f:
                f.append(d['teacher'])
                main_list.append({
                    'faculty': d['faculty_id'],
                    'teacher': d['teacher'],
                    'name': d['period'],
                    'line': [],
                    'class': d['class'],
                })
                for m in main_list:
                    if m['teacher'] == d['teacher']:
                        m['line'].append({d['day']: d})

            else:
                for m in main_list:
                    if m['teacher'] == d['teacher']:
                        m['line'].append({d['day']: d})

        return main_list
    #it returns the weekdays from sunday to thursday
    def get_heading(self):
        dayofWeek = [_(calendar.day_name[6]),
                     _(calendar.day_name[0]),
                     _(calendar.day_name[1]),
                     _(calendar.day_name[2]),
                     _(calendar.day_name[3]),
                    # _(calendar.day_name[4]),
                    # _(calendar.day_name[5]),
                     ]
        return dayofWeek
    #here all sessions data feth and storing dictionary wise in a list called data_list.
    def get_object(self, data):
        data_list = []
        for timetable_obj in self.env['op.session'].browse(
                data['teacher_time_table_ids']):
            oldDate = pytz.UTC.localize(
                fields.Datetime.from_string(timetable_obj.start_datetime))
            day = datetime.weekday(oldDate)
            timetable_data = {
                'period': timetable_obj.timing_id.name,
                'period_time': timetable_obj.timing_id.hour + ':' +
                timetable_obj.timing_id.minute +
                timetable_obj.timing_id.am_pm,
                'sequence': timetable_obj.timing_id.sequence,
                'day': str(day),
                'subject': timetable_obj.subject_id.name,
                'course': timetable_obj.course_id.name,
                'batch': timetable_obj.batch_id.name,
                'faculty_id': timetable_obj.faculty_id.name,
                'teacher': timetable_obj.faculty_id.name,
                'class': timetable_obj.classroom_id.name,
            }
            data_list.append(timetable_data)
        ttdl = sorted(data_list, key=lambda k: k['sequence'])
        final_list = self.sort_tt(ttdl)
        return final_list

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
            'get_object': self.get_object,
            'get_heading': self.get_heading,
            'get_full_name': self.get_full_name,
        }
        return docargs