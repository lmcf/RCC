# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 15:16:38 2022

@author: calde
"""

import xml.etree.ElementTree as ET

def get_literal( name = 'error_literal', parent = 'LITERALES'):
     literal_txt = ''
     CONFIG = ET.parse('conf\\conf.xml').getroot()
     for element in  CONFIG.findall(parent):
             literal_txt = element.find(name).text
             
     return literal_txt
    
def get_log_path( name ):
    parent = 'LOGS'
    return get_literal(name, parent)

PATH_DEBUG  = get_log_path('path_debug')
PATH_ERROR  = get_log_path('path_error')
PATH_INFO   = get_log_path('path_info')
PATH_WARN   = get_log_path('path_warn')
NAME_DEBUG  = get_log_path('name_debug')
NAME_ERROR  = get_log_path('name_error')
NAME_INFO   = get_log_path('name_info')
NAME_WARN   = get_log_path('name_warn')


