from threading import Lock,Thread
from colorama import Fore
import requests
import elementos as el
import funciones as func
from keyboard import is_pressed
import params

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
        self.html = None
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

    def obtener_html(self):
        if self.validado:
            self.html = requests.get(self.url).text


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
                            func.subdom_reemplazo(palabra=palabra,reemp=x,head=self.head,url=self.url,obj_html=self.html)
                        except:
                            pass
                        finally:
                            func.n += 1
                    else:
                        break        
            else:
                print(Fore.GREEN+'buscando subdominios')
                for x in self.lista:
                    
                    Thread(target=func.masivo,args=(x,self.html)).start()
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
                            func.rutas(x=x,url=self.url,time=5,head=self.head,obj_html=self.html)
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
                        
                        Thread(target=func.masivo,args=(x,self.html)).start()
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
    url.obtener_html()
    url.lectura()
    if params.param.subdom:
        url.subdom()
    else:
        url.rutas()
    
    