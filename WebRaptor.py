import requests
from colorama import Fore
from threading import Thread,Lock
from keyboard import is_pressed
import funciones as func
import params
import elementos as el



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


    def subdom(self):

        if self.validado and self.leido:
            if params.param.lineal:
                print(Fore.GREEN+'buscando subdominios: metodo lineal (baja carga)')
            #detectar palabra a cambiar
                Thread(target=func.progreso,args=(self.nombre_dic,)).start()

                palabra = self.url.split('//')[-1].split('.')[0]
                for x in self.lista:
                    if not func.detenido:
                        try:
                            func.subdom_reemplazo(palabra=palabra,reemp=x,head=self.head,url=self.url)
                        except:
                            pass
                        finally:
                            func.n += 1
                    else:
                        break        
            else:
                print(Fore.GREEN+'buscando subdominios')
                for x in self.lista:
                    
                    Thread(target=func.masivo,args=(x,)).start()
                    if is_pressed('esc'):
                        print(Fore.RED+'deteniendo...')
                        func.detenido = True
                        break
                    

    def lectura(self):
        if self.validado and self.lista != None:
            
            print(Fore.CYAN+f'utilizando el diccionario: {self.nombre_dic}')
            self.leido = True
        else:
            print(Fore.RED+'no se pudo leer el diccionario')


    
    def rutas(self):
        #se ejecuta la busqueda de rutas
        if self.leido and self.validado:

            #ejecucion lineal----------------------------
            if params.param.lineal and self.lista != None and not ',' in self.nombre_dic:
                print(Fore.GREEN+'buscando rutas: metodo lineal (baja carga)')
                Thread(target=func.progreso,args=(self.nombre_dic,)).start()

                for x in self.lista:
                    if not func.detenido:
                        
                        try:                    
                            func.rutas(x=x,url=self.url,time=5,head=self.head)
                        except:
                            continue
                
                        finally:
                            func.n += 1
                            if params.param.guardar:
                                func.guardar(diccionario=self.nombre_dic)
            #ejecucion masiva----------------------------
            else:
                if self.lista != None:
                    print(Fore.GREEN+'buscando rutas')
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

def crear_obj(url_,timeout,lista,dic):
    
    url = Url(url_or=url_,timeout=timeout,lista=lista,dic=dic)
    url.validacion()
    url.lectura()
    if params.param.subdom:
        url.subdom()
    else:
        url.rutas()

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
            # aca iria la funcion para poner varios dicionarios para subdom tambien (cosa a hacer en el futuro)
            if not params.param.subdom:
                for x in params.param.dic.split(','):
                    lista = func.lectura_dic(x)
                    
                    crear_obj(url_=params.param.url,timeout=timeout,lista=lista,dic=x)
        else:
            lista = func.lectura_dic(params.param.dic)

            crear_obj(url_=params.param.url,timeout=timeout,lista=lista,dic=params.param.dic)
            

    except TypeError:
        pass