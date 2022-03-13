# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:36:47 2022

@author: calde
"""
from functions import *
data = {
       'msg':'INICIO :: {} del archivo {}',
       'args' : [
           'Prueba',
           __file__
       ]
}

msglog(data,l.NAME_INFO)





closeLogging()