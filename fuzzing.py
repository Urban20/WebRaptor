import requests
from colorama import Fore
from threading import Thread
from keyboard import is_pressed
import funciones as func
import params
import elementos as el


print(el.logo)

class Url():
    def __init__(self,url_or,timeout):
        #url original
        self.url = url_or
        self.validado = False
        self.head = el.data
        self.leido = False
        self.timeout = timeout

    def validacion(self):
        try:
            sitio = requests.get(self.url,timeout=self.timeout,headers=self.head)
            if sitio.status_code == 200:
                self.validado = True
            else:
                print(Fore.RED+f'el sitio no responde, codigo de estatus:{sitio.status_code}')
                print(el.status[sitio.status_code])
        except TimeoutError:
             print(Fore.RED+'tiempo de espera agotado')
        except Exception as e:
            print(Fore.RED+f'error: {e}')

    def lectura(self,lista,dic):
        if self.validado and lista != None:
            
            print(Fore.CYAN+f'utilizando el diccionario: {dic}')
            self.leido = True
        else:
            print(Fore.RED+'no se pudo leer el diccionario')



    def ejecucion(self,lista:list):
        
        if self.leido and self.validado:
            if params.param.lineal and lista != None:
            
                Thread(target=func.progreso).start()

                for x in lista:
                    if not func.detenido:
                        ruta = f'{self.url}{x}'
                        try:                    
                            test= requests.get(self.url+ x,timeout=5,headers=self.head)

                            if test.status_code == 200:
                                print(Fore.WHITE+ruta)
                                    
                                el.encontrado.append(ruta)

                            elif test.status_code == 401:
                                print(Fore.YELLOW+f'requiere autorizacion:{x}')
                                    
                                el.encontrado.append(ruta)
                        except:
                            continue
                
                        finally:
                            func.n += 1
                            if params.param.guardar:
                                func.guardar(params.param.dic)
            else:
                if lista != None:
                    for x in lista:
                        
                        Thread(target=func.masivo,args=(x,)).start()
                        if is_pressed('esc'):
                            print(Fore.RED+'deteniendo...')
                            func.detenido = True
                            break
                else:
                    print(Fore.RED+'no se pudo procesar el diccionario correctamente')

if params.param.timeout != None:
    timeout = params.param.timeout
else:
    timeout = 5

url = Url(url_or=params.param.url,timeout=timeout)
url.validacion()
lista = func.lectura_dic(params.param.dic)
url.lectura(lista=lista,dic=params.param.dic)
url.ejecucion(lista=lista)