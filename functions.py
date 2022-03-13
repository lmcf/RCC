# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 15:09:41 2022

@author: calde
"""

from logger import Logs
import literales as l
import logging

def msglog(msg, logger):
   if(logger == l.NAME_WARN):
        path = l.PATH_WARN
   elif(logger == l.NAME_INFO):
       path = l.PATH_INFO
   elif(logger == l.NAME_ERROR):
       path = l.PATH_ERROR
   else:
       path = l.PATH_DEBUG

   X = Logs(logger, path)
   X.msg(msg)
   
def closeLogging():
    logging.shutdown()