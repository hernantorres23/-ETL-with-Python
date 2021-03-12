# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:53:52 2019

@author: hernan
"""

try:
    import httplib
except:
    import http.client as httplib
import socket
import sys
#import http.client as httplib

def have_internet():
    conn = httplib.HTTPConnection('www.google.com', timeout=3)
    try:
        conn.request('HEAD', '/')
        print("Conectado")
        conn.close()
        return True
    except socket.gaierror:
        print('Sin conexion a internet')
        conn.close()
        #sys.exit()
        return False
    except httplib.HTTPConnection:
        print("Sin conexion a internet")
        conn.close()
        #sys.exit()
        return False    

#for test use the next line
#have_internet()


##def hayinternet():
##    s = socket.socket()
##    s.settimeout(5)   # 5 seconds
##    try:
##        s.connect(('40.101.96.2', 443))         # una direccion IP para comprobar la direccion a internet
##        print('El test de conexion a internet, fue realizado exitosamente')
##        return True
##    except socket.error as exc:
##        print("No tiene conexion a internet : %s" % exc)
##        return False
##
##hayinternet()
