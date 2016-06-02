# -*- coding: utf-8 -*-
##############################################################################
from openerp.osv import fields, osv
from openerp import api
#Importamos la libreria logger
import logging
from datetime import  datetime
from time import time
#Definimos la Variable Global
_logger = logging.getLogger(__name__)

class report_report_bienes_wizard(osv.osv_memory):
    _name="report.report_bienes_wizard"
    _columns={
              'oficinas_id':fields.many2one('oficinas',"Oficinas",required=True),
              'fecha_imp':  fields.date("Fecha del Inventario", required=True ),
              'ban':fields.char('Ban',size = 4),
              }

_defaults={
                'ban':'PASE'
            }
            
def check_report(self, cr, uid, ids, context=None):
        data={}
        data['model']='oficinas','report_report_bienes_wizard'
        data['ids']=ids
        data['origin_records']=False
        data.update({'parameters':{
                            'report_title':"Reporte Bienes con jasper",
                            'oficinas_id':self.browse(cr,uid,ids[0]).oficinas_id.id,
                            'fecha_imp': time.strftime('%d-%m-%y',self.browse(cr,uid,ids[0]).fecha_imp),
                            
                }


                  })
        r= {
                'type':'ir.actions.report.xml',
                'report_name':'report_bienes',
                'datas':data
        }
        return r

report_report_bienes_wizard()
