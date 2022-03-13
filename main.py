# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:36:47 2022

@author: calde
"""
from logger import Logs
import literales as lt
import logging

def msglog(msg, logger):
   if(logger == lt.NAME_WARN):
        path = lt.PATH_WARN
   elif(logger == lt.NAME_INFO):
       path = lt.PATH_INFO
   elif(logger == lt.NAME_ERROR):
       path = lt.PATH_ERROR
   else:
       path = lt.PATH_DEBUG

   X = Logs(logger, path)
   X.msg(msg)
    
    
msglog("Laurita ",lt.NAME_DEBUG)

msglog("",lt.NAME_ERROR)

msglog("info mode",lt.NAME_INFO)

msglog("info mode",lt.NAME_WARN)


logging.shutdown()