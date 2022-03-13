# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 13:28:11 2022

@author: LM Caldeiro
"""
import logging

class Logs():
    def __init__(self,name, log_file):
        self.formatter = logging.Formatter('%(asctime)s  %(message)s')
        self.name = name
        self.logger = self.setup_logger(name, log_file)
    
    def setup_logger(self, name, log_file, level=logging.INFO):
        """To setup as many loggers as you want"""
    
        handler = logging.FileHandler(log_file)        
        handler.setFormatter(self.formatter)
    
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
    
        return logger
    
    def msg(self, msg = ''):
       print("NAME LOGGER %s" % self.name)
       self.logger.info(msg)
       handlers = self.logger.handlers[:]
       for handler in handlers:
           handler.close()
           self.logger.removeHandler(handler)
       
       
    







