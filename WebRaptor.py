import funciones as func
import params
import elementos as el
import clases
from colorama import Fore

try:
    if params.param.timeout != None:
        timeout = params.param.timeout
    else:
        timeout = 5

    if params.param.ayuda:
        func.ayuda()

    elif params.param.url != None or params.param.dic != None:

        print(el.logo)

        try:
            # cuando tenes muchos diccionarios con los que probar
            if ',' in params.param.dic:
              
                
                for x in params.param.dic.split(','):
                    lista = func.lectura_dic(x)
                    
                    clases.crear_obj(url_=params.param.url,timeout=timeout,lista=lista,dic=x)
            else:
                lista = func.lectura_dic(params.param.dic)

                clases.crear_obj(url_=params.param.url,timeout=timeout,lista=lista,dic=params.param.dic)
                

        except TypeError:
            pass
except KeyboardInterrupt:
    print(Fore.RED+'interrumpiendo script')
    func.detenido = True
    exit()