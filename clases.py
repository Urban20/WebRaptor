from threading import Lock
from colorama import Fore
import requests
import elementos as el
import funciones as func
import params
from concurrent.futures import ThreadPoolExecutor



def detencion():
    print(Fore.RED+'deteniendo...')
    func.detenido = True

#numero de hilos que lleva el scrip
if params.param.hilos != None:
    
    hilo = params.param.hilos

else:
    hilo = 16

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
            self.validado = True
            
        except TimeoutError:
             print(Fore.RED+'tiempo de espera agotado')
             exit(1)
        except Exception as e:
            print(Fore.RED+f'error: {e}')
            exit(1)

    def obtener_html(self):
        if self.validado:
            self.html = requests.get(self.url).text


    def subdom(self,hilo):

        if self.validado and self.leido:
           
            print(Fore.GREEN+'buscando subdominios')
            
            print(f'utilizando {hilo} hilos')

            with ThreadPoolExecutor(max_workers=hilo) as ejec:
                
                for x in self.lista:
                    
                    ejec.submit(func.masivo,x,self.html)

                        
    def lectura(self):
        if self.validado and self.lista != None:
            
            print(Fore.CYAN+f'utilizando el diccionario: {self.nombre_dic}')
            self.leido = True
        else:
            print(Fore.RED+'no se pudo leer el diccionario')


    
    def rutas(self):
        #se ejecuta la busqueda de rutas
        if self.leido and self.validado:
            
            #ejecucion masiva----------------------------
            
            if self.lista != None:
                print(Fore.GREEN+'buscando rutas')
                print(f'utilizando {hilo} hilos')
                with ThreadPoolExecutor(max_workers=hilo) as ejec:
                    for x in self.lista:
                       
                        ejec.submit(func.masivo,x,self.html)
                        
                        

            else:
                print(Fore.RED+'no se pudo procesar el diccionario correctamente')


def crear_obj(url_,timeout,lista,dic):
    
    url = Url(url_or=url_,timeout=timeout,lista=lista,dic=dic)
    url.validacion()
    url.obtener_html()
    url.lectura()
    if params.param.subdom:
        url.subdom(hilo=hilo)
    else:
        url.rutas()
    
    