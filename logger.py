# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 13:28:11 2022

@author: LM Caldeiro
"""

import xml.etree.ElementTree as ET
import logging
import os
import datetime



class Logs:
  
    def __init__(self,name, filetrack = __file__ ):
        self.filetrack = filetrack
        self.name = name
        self.extra = {'user': os.getlogin()}
        self.CONFIG_PATH = 'conf\\conf.xml'
        self.CONFIG = ET.parse(self.CONFIG_PATH).getroot()
        self.logger = self.setup_logger(self.name, self.get_log_path(self.name))
        
    
    def msg(self, message = '', literal = 'error_literal'):
        
        if(message == ''  and  literal != 'error_literal'):
            message = self.return_literal(literal)
            
        elif(message == '' and literal == 'error_literal'):
            message = self.return_literal('error_literal')
                    
        # Preparamos mensaje de log
        ct = datetime.datetime.now() 
        message = " ##### %s ##### %s " % (ct, message)
        
       
        self.logger.debug(message,extra=self.extra);
        self.logger.shutdown()
             

    def setup_logger(self, name, log_file, log_level='debug'):
        logging.getLogger(name)
        if (log_level == 'debug'):
            log_level = logging.DEBUG
        elif (log_level == 'error'):
            log_level = logging.ERROR
        else:
            log_level = logging.WARN
            
        logging.basicConfig(filename=log_file, level=log_level)
        
        return logging
        
    
    def get_log_path(self, name):
        parent_name = 'LOGS'
        return self.return_literal(name, parent_name)
       
    def return_literal(self, name = 'error_literal' ,parent = 'LITERALES',):
        literal_txt = ''
        for element in  self.CONFIG.findall(parent):
                literal_txt = element.find(name).text
                
        return literal_txt



        





