# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:36:47 2022

@author: calde
"""
from functions import msglog, closeLogging
import literales as l

#msglog f
msglog("Laurita ",l.NAME_DEBUG)

msglog("Error mode",l.NAME_ERROR)

msglog("info mode",l.NAME_INFO)

msglog("warm mode",l.NAME_WARN)


closeLogging()