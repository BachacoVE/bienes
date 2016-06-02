# -*- coding: utf-8 -*-
##############################################################################
 
class JasperDataParser(object):
   def __init__(self, cr, uid, ids, data, context):
        if not context: context = {}
        self.cr = cr
        self.uid = uid
        self.ids = ids
        self.data = data
        self.context = context
     
   def get(self,parameter,default_value):
        if(parameter=="ids"):
            return hasattr(self, 'generate_ids') and \
                self.generate_ids(self.cr, self.uid, self.ids, self.data, self.context) or default_value
        elif parameter == 'name':
            return hasattr(self, 'generate_name') and \
                 self.generate_name(self.cr, self.uid, self.ids, self.data, self.context) or default_value
        elif parameter == 'model':
            return hasattr(self, 'generate_model') and \
                 self.generate_model(self.cr, self.uid, self.ids, self.data, self.context) or default_value
        elif parameter == 'records':
            return hasattr(self, 'generate_records') and \
                 self.generate_records(self.cr, self.uid, self.ids, self.data, self.context) or default_value
        elif parameter == 'data_source':
            return hasattr(self, 'generate_data_source') and \
                self.generate_data_source(self.cr, self.uid, self.ids, self.data, self.context) or default_value
        elif parameter == 'parameters':
            return hasattr(self, 'generate_parameters') and \
                self.generate_parameters(self.cr, self.uid, self.ids, self.data, self.context) or default_value
        elif parameter == 'properties':
            return hasattr(self, 'generate_properties') and \
                self.generate_properties(self.cr, self.uid, self.ids, self.data, self.context) or default_value
        else: return default_value
         
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
