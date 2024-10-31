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

def lectura_dic(dicc):
    try:
        with open(f'diccionarios/{dicc}','r') as diccionario:
            return str(diccionario.read()).split()
    except FileNotFoundError:
        print(Fore.RED+'diccionario no encontrado')
def guardar(diccionario):
    try:
        if el.encontrado: 
            with open(f'{str(params.param.url).split('/')[2]}-{diccionario.split('.')[0]}.txt','w') as registro:
                registro.write('''urls encontradas: 
                ''')
                for i in el.encontrado:
                    registro.write(f'''

    {i}

                        ''')
    except Exception as e:
        print(f'ocurrio un error:{e}')
    
def progreso():
    global n
    global detenido
    #cantidad total de elementos en la lista
    try:
        lista = func.lectura_dic(params.param.dic)
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
            
            ruta = f'{params.param.url}{x}'
            
            
            test= requests.get(ruta,timeout=2,headers=el.data)

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
        except:
            pass
        finally:
            if params.param.guardar:
                guardar(params.param.dic)


