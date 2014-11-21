from openerp.osv import osv
from openerp.osv import fields

class net_usage(osv.osv):

    _name = 'net.usage'
    _description = 'net.usage'
    
    def get_reste(self, cr, uid, ids, name, arg, context):
        x = {}
        for record in self.browse(cr, uid, ids ,context):
            
                x[record.id]= record.ncs_download + record.ncs_upload
        return x
 
    _columns = {                       
               
                'ncs_starttime': fields.datetime('Start Time'),
                'ncs_stoptime': fields.datetime('Stop Time'), 
                'ncs_download': fields.integer('Download (KB)'),
                'ncs_upload': fields.integer('Upload (KB)'),
                'ncs_total': fields.function(get_reste, type='integer', method='True', string='Total Units (KB)'),    
                'ncs_duration':fields.char('Duration', size=64, required=False, readonly=False),
               
                }
net_usage()

