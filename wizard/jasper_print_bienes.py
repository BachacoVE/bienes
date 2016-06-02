# -*- coding: utf-8 -*-
############################################################################
from openerp.addons.jasper_reports import jasper_report
from openerp import pooler
from openerp.addons.bienes import jasper_data_parser
 
class jasper_print_bienes(jasper_data_parser.JasperDataParser):
     
    def __init__(self, cr, uid, ids, data, context):
        if context is None:
            context = {}
        super(jasper_print_product,self).__init__(cr, uid, ids, data, context)
     
    def generate_records(self, cr, uid, ids, data, context):
            return []
                 
    def generate_data_source(self, cr, uid, ids, data, context):
        if not(data['origin_records']):
            return False
        else:
            return 'records'
     
    def generate_parameters(self, cr, uid, ids, data, context):
        return data.get('parameters',True)
 
jasper_report.report_jasper(
                            'report.report_bienes', 
                            'oficinas',
                            parser=jasper_print_bienes
                            
                            )
