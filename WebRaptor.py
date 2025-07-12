#! /usr/bin/env -S python3

import funciones as func
import params
import elementos as el
import clases
from colorama import Fore
import signal
import sys
from os import devnull

# autor : Urban
# aclaracion importante: el codigo esta un poco desorganizado con variables que pueden ser confusas, codigo redundante , tambien puede haber metodos y funciones que se llaman igual
# el codigo es algo viejo, pero funciona y se intenta pulir y mejorar en la medida de lo posible

sys.stderr = open(devnull,'w')

try:

    if not params.param.ayuda:
        print(el.logo)

    #no funciona del todo bien, revisar
    signal.signal(signalnum=signal.SIGINT,handler=func.salir)

    if params.param.timeout != None:
        timeout = params.param.timeout
    else:
        timeout = 5

    if params.param.ayuda:
        func.ayuda()
    
    elif params.param.url != None or params.param.dic != None:

        

        try:
            
            for x in params.param.dic.split(','):
                lista = func.lectura_dic(x)
                
                clases.crear_obj(url_=params.param.url,timeout=timeout,lista=lista,dic=x)
    
                

        except TypeError:
            pass
except KeyboardInterrupt:
    print(Fore.RED+'interrumpiendo script')
    func.detenido = True
    sys.exit(0)