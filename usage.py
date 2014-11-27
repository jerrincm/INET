from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class net_usage(osv.osv):

    _name = 'net.usage'
    _description = 'net.usage'
    
    def get_reste(self, cr, uid, ids, name, arg, context):
        x = {}
        for record in self.browse(cr, uid, ids ,context):
            
                x[record.id]= record.ncs_download + record.ncs_upload
        return x
    
   
    
    def onchange_return_date(self, cr, uid, ids, issuedate, returndate):
        a=False
        b=False
        total= False
        if issuedate and returndate:
            a=datetime.strptime(issuedate,"%Y-%m-%d %H:%M:%S")
            b=datetime.strptime(returndate,"%Y-%m-%d %H:%M:%S")        
            hour = relativedelta(b, a).hours
            minutes = relativedelta(b, a).minutes
            seconds = relativedelta(b, a).seconds
            total = ("%s:%s:%s")%(hour,minutes,seconds)            
        return {'value': {'ncs_duration':total}}
 
    _columns = {                       
               
                'ncs_starttime': fields.datetime('Start Time'),
                'ncs_stoptime': fields.datetime('Stop Time'), 
                'ncs_download': fields.integer('Download (KB)'),
                'ncs_upload': fields.integer('Upload (KB)'),
                'ncs_total': fields.function(get_reste, type='integer', method='True', string='Total Units (KB)'),    
                'ncs_duration':fields.char('Duration', size=64, required=False, readonly=False),
               
                }
net_usage()

