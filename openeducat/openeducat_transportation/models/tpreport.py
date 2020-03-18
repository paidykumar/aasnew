from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class TransportReport(models.TransientModel):
    _name = 'isk.report'
    name = fields.Char('Name', size=64, required=True)
    vehicle = fields.Many2one('op.transportation', 'Vehicle', required=True)

    @api.multi

    def get_report(self):
        """Call when button 'Get Report' clicked.
        """

        data = {
            'ids': self.ids,
            'model': self._name,
            'name': self.name,
            'vehicle': self.vehicle,
        }

        # use `module_name.report_id` as reference.
        # `report_action()` will call `get_report_values()` and pass `data` automatically.
        return self.env.ref('openeducat_transportation.recap_report').report_action(self, data=data)


class ReportAttendanceRecap(models.AbstractModel):
    """Abstract Model for report template.

    for `_name` model, please use `report.` as prefix then add `module_name.report_name`.
    """

    _name = 'report.openeducat_transportation.attendance_recap_report_view'

    @api.model
    def get_report_values(self, docids, data=None):

        docs = []
        stops = self.env['op.stop'].search([], order='name asc')
        connection = None
        for stop in stops:

            docs.append({
                'stop': stop.name,
                'connection': stop.sequence,

            })
            students = []
            studentsob = self.env['op.student'].search([], order='name asc')
            sname = None
            sid = None
            scontact = None
            slastname=None
            for student in studentsob:

                students.append({'scontact':(student.emergency_contact.phone),
                                 'slastname':student.last_name,
                                 'sid':student.id_number})
            transport = []
            transportob = self.env['op.transportation'].search([], order='name asc')
            tname = None
            tvehicle = None
            tfrom = None
            tto = None
            tstarttime=None
            tendtime=None
            #vehicle=None
            vname = (data['vehicle']),
                #self.env['isk.report'].search([('vehicle', '=', '')], limit=1)
            for tp in transportob:
                #if data['form']['vehicle']==(tp. vehicle_id.name):
                    transport.append({'tname': tp,
                                      'tvehicle': (tp. vehicle_id.name),
                                      'tfrom': (tp.from_stop_id.name),
                                      'tto': (tp.to_stop_id.name),
                                      'tstarttime':tp.start_time,
                                      'tendtime':tp.end_time,
                                      'tvname':vname,})



        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'docs': docs,
            'students' : students,
            'transport':transport,

        }
