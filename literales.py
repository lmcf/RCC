# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 15:16:38 2022

@author: calde
"""

import xml.etree.ElementTree as ET
import os

# Devuelve literal de la configuración en base al hijo y padre. Teniendo como root config
def get_literal( name = 'error_literal', parent = 'LITERALES'):
     literal_txt = ''
     
     if(os.name == 'nt'):
         conf_url ='conf\\conf.xml'
     else:
         conf_url = 'conf/conf.xml'
         
     CONFIG = ET.parse(conf_url).getroot()
     for element in  CONFIG.findall(parent):
             literal_txt = element.find(name).text
             
     return literal_txt
 
# Devuele información de tag dentro de LOGS
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


# CONST
# COLORS
COLOR_SUCCESS = '#00ff00'   # Green
COLOR_INACTIVE = '#ffff66'  # Yellow
COLOR_DANGER = '#ff0000'    # Red
COLOR_DANGER_ACTIVE = '#cc0000' # Darker red
COLOR_WHITE = '#fff'
COLOR_BLACK = '#000'
COLOR_INTERMITENTE = '#FFC300'
COLOR_DISABLED = '#a1a5ab'
BG_COLOR = '#f5f5dc'

# FONTS
FONT_STYLE_TXT = ('Helvetica' , 14)
FONT_STYLE_TITLE = ('Helvetica' , 16, 'bold')

#BUTTONS
BTN_SYSTEM_WIDTH = 10

#LABELS
LBL_FIXED_WIDTH = 15
LBL_SQUARE_WIDTH_HEIGHT = 5