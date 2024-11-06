from time import time
from keyboard import is_pressed
import elementos as el
from colorama import init, Fore
import requests
import params
import funciones as func

init()
n = 0
detenido = False


def rutas(x,url,time,head):
    ruta = f'{url}{x}'
                
    test= requests.get(ruta,timeout=time,headers=head)

    if test.status_code == 200:
        print(Fore.WHITE+ruta)
        if params.param.guardar:
            with el.lock:   
                el.encontrado.append(ruta)

    elif test.status_code == 401:
        print(Fore.YELLOW+f'requiere autorizacion:{ruta}')
        if params.param.guardar:
            with el.lock:
                el.encontrado.append(ruta)


def subdom_reemplazo(palabra,url,head,reemp):
    url_exp = url.replace(palabra,reemp)
    test= requests.get(url_exp,headers=head)
    
    if test.status_code == 200:
        print(Fore.WHITE+url_exp)
    elif test.status_code == 401:
        print(Fore.YELLOW+f'requiere autorizacion: {url_exp}')

    if params.param.guardar:
        with el.lock:
            el.encontrado.append(url_exp)
        guardar(params.param.dic)


def ayuda():
    print(Fore.CYAN+ r'''    
                
{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
{}                                                    {}
{}                                                    {}
{}      █████╗ ██╗   ██╗██╗   ██╗██████╗  █████╗      {}
{}     ██╔══██╗╚██╗ ██╔╝██║   ██║██╔══██╗██╔══██╗     {}
{}     ███████║ ╚████╔╝ ██║   ██║██║  ██║███████║     {}
{}     ██╔══██║  ╚██╔╝  ██║   ██║██║  ██║██╔══██║     {}
{}     ██║  ██║   ██║   ╚██████╔╝██████╔╝██║  ██║     {}
{}     ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝  ╚═╝     {}
{}                                                    {}
{}                                                    {}
{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
          
    ''')
    
          
    print(Fore.GREEN+'Uso:') 
    print(Fore.WHITE+'''    
wr --url [url] --dic [dic]
          
-h o --ayuda para desplegar la ayuda

creado por urb@n para descubrir rutas ocultas en paginas web.
Consiste en buscar directorios ocultos a partir de un diccionario proporcionado por el usuario con el objetivo de encontrar archivos o vulnerabilidades

parametros obligatorios:
url                             *url de la web a hacer fuzzing
          
dic                             *diccionario en formato .txt que se utiliza para hacer fuzzing, debe estar escrito en formato de listado

--> el parametro dic admite varios diccionarios, para usar esta función se debe pasar el nombre de los diccionarios terminados en .txt y separarlos con "," entre sí          
''')
    print(Fore.GREEN+'opciones:')
    print(Fore.WHITE+'''        
-h, --ayuda                     *muestra este mensaje
        
-g, --guardar, --no-guardar     *argumento opcional para guardar las urls en caso de encontrarse alguna
        
-l, --lineal, --no-lineal       *argumento opcional para la busqueda de directorios de forma lineal (consume menos recursos del cpu)
                                 solo funciona cuando se pasa como parametro un solo diccionario                       
          
-t TIMEOUT, --timeout TIMEOUT   *tiempo de tolerancia del script para conectarse a una url
          
-sd, --subdom                   *busqueda de subdominios en sitios web
      
''')
    print('''
#########################################################################################################''')
    print(Fore.MAGENTA+el.titulo)



def lectura_dic(dicc):
    try:
        with open(f'diccionarios/{dicc}','r') as diccionario:
            return str(diccionario.read()).split()
    except FileNotFoundError:
        print(Fore.RED+'diccionario no encontrado')


def guardar(diccionario):
    try:
        if el.encontrado: 
            if params.param.subdom:
                nombre = f'{str(params.param.url).split('/')[2]}-{diccionario}-subdoms.txt'
            else:
                nombre = f'{str(params.param.url).split('/')[2]}-{diccionario}.txt'

            with open(nombre,'w') as registro:
                registro.write('''urls encontradas: 
                ''')
                for i in el.encontrado:
                    registro.write(f'''

    {i}

                        ''')
    except Exception as e:
        print(f'ocurrio un error:{e}')
    

def progreso(diccionario):
    global n
    global detenido
    #cantidad total de elementos en la lista
    try:
        lista = func.lectura_dic(diccionario)
        tamaño_list_i = len(lista)
        tiempo = time()
        while not detenido:
        
            val_prog = (n/tamaño_list_i) * 100
            porcentaje =f'{str(val_prog)[:5]}%'
            if is_pressed('esc'):
                print(Fore.RED+'detenido')
                detenido = True
                
            if time() - tiempo > 1:
                print(Fore.CYAN+f'progreso: {porcentaje}')
                tiempo = time()
            if porcentaje == '100.0%':
                print(Fore.GREEN+'script finalizado')
                detenido = True
    except Exception as e:
        print(f'ocurrio un error: {e}')


def masivo(x):
    global detenido
    if not detenido:
        try:
            #cuando no hay parametro -sd
            if not params.param.subdom:

                rutas(x=x,url=params.param.url,time=2,head=el.data)

            #cuando si lo hay
            else:
                try:
                    
                    palabra = params.param.url.split('//')[-1].split('.')[0]
                    
                    subdom_reemplazo(palabra=palabra,url=params.param.url,head=el.data,reemp=x)

                except:
                    pass


        except:
            pass
        

