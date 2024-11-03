import requests
from colorama import Fore
from threading import Thread,Lock
from keyboard import is_pressed
import funciones as func
import params
import elementos as el


#nota: hacer opciones para encontrar subdominios

class Url():
    def __init__(self,url_or,timeout,lista,dic):
        #url original
        self.url = url_or
        self.validado = False
        self.head = el.data
        self.leido = False
        self.timeout = timeout
        self.lista = lista
        self.nombre_dic = dic
        self.lock = Lock

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

    def lectura(self):
        if self.validado and self.lista != None:
            
            print(Fore.CYAN+f'utilizando el diccionario: {self.nombre_dic}')
            self.leido = True
        else:
            print(Fore.RED+'no se pudo leer el diccionario')



    def ejecucion(self):
        
        if self.leido and self.validado:

            #ejecucion lineal----------------------------
            if params.param.lineal and self.lista != None and not ',' in params.param.dic:
                
                    Thread(target=func.progreso,args=(params.param.dic,)).start()

                    for x in self.lista:
                        if not func.detenido:
                            ruta = f'{self.url}{x}'
                            try:                    

                                test= requests.get(self.url+ x,timeout=5,headers=self.head)

                                if test.status_code == 200:
                                    print(Fore.WHITE+ruta)
                                        
                                    with self.lock:   
                                        el.encontrado.append(ruta)

                                elif test.status_code == 401:
                                    print(Fore.YELLOW+f'requiere autorizacion:{x}')


                                    with self.lock:    
                                        el.encontrado.append(ruta)
                            except:
                                continue
                    
                            finally:
                                func.n += 1
                                if params.param.guardar:
                                    func.guardar(diccionario=self.nombre_dic)
            #ejecucion masiva----------------------------
            else:
                if self.lista != None:
                    for x in self.lista:
                        
                        Thread(target=func.masivo,args=(x,)).start()
                        if is_pressed('esc'):
                            print(Fore.RED+'deteniendo...')
                            func.detenido = True
                            break
                        if params.param.guardar:
                            func.guardar(diccionario=self.nombre_dic.split('.')[0])

                else:
                    print(Fore.RED+'no se pudo procesar el diccionario correctamente')



if params.param.timeout != None:
    timeout = params.param.timeout
else:
    timeout = 5



if params.param.ayuda:
    func.ayuda()
elif params.param.url != None or params.param.dic != None:

    print(el.logo)

    try:
        if ',' in params.param.dic:
            for x in params.param.dic.split(','):
                lista = func.lectura_dic(x)
                url = Url(url_or=params.param.url,timeout=timeout,lista=lista,dic=x)
                url.validacion()
                url.lectura()
                url.ejecucion()
        else:
            lista = func.lectura_dic(params.param.dic)
            url = Url(url_or=params.param.url,timeout=timeout,lista=lista,dic=params.param.dic)
            url.validacion()
            url.lectura()
            url.ejecucion()
    except TypeError:
        pass