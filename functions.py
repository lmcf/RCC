# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 15:09:41 2022

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
