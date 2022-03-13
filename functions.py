# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 15:09:41 2022

@author: calde
"""

from logger import Logs, logging
import literales as l


## Función para setear el mensaje y hacer la petición al logger
def msglog(data, logger):
   if(logger == l.NAME_WARN):
        path = l.PATH_WARN
        extra = '## WARN :: '
   elif(logger == l.NAME_INFO):
       path = l.PATH_INFO
       extra = '## INFO :: '
   elif(logger == l.NAME_ERROR):
       path = l.PATH_ERROR
       extra = '## ERROR :: '
   else:
       path = l.PATH_DEBUG
       extra = '## DEBUG :: '
       
   data['extra'] = extra   
   
   X = Logs(logger, path)
   msg = createMsg(data)
   X.msg(msg)
 
# Función para "apagar" todos los loggers   
def closeLogging():
    logging.shutdown()
 
# Función para validar los argumentos de la data del mensaje
def validateMsg(data):
    validKeys = ['msg', 'args', 'extra']
    valid = True
    for item in validKeys:
        if(item not in data):
            return False
    
    return valid

# Función que formata el mensaje y lo devuelve
def createMsg(data):
   if(validateMsg(data)):
      msg = data['msg'] 
      args = data['args']
      extra = data['extra']
      
      msg = extra+msg
      
      msg = msg.format(*args)
      
      return msg
       
   else:
       error = {
               'msg':'ERROR :: Fallo en la validacion de los parametros al crear el log => {}',
               'args' : [data]
               }

       msglog(error,l.NAME_ERROR)
        