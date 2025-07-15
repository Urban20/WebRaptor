import argparse


args = argparse.ArgumentParser(
    prog='WebRaptor',
    usage='''wr [url] [dic]
    -h o --ayuda para desplegar la ayuda ''',

    description= 'creado por urb@n para descubrir rutas ocultas en paginas web',add_help=False
    
    )

args.add_argument('--url',type=str,help='url de la web a hacer fuzzing')
args.add_argument('--dic',type=str,help='diccionario en formato .txt que se utiliza para hacer fuzzing, debe estar escrito en formato de listado')
args.add_argument('-g','--guardar',help='argumento opcional para guardar las urls en caso de encontrarse alguna',action=argparse.BooleanOptionalAction)
args.add_argument('-t','--timeout',type=int,help='tiempo de tolerancia del script para conectarse a una url')
args.add_argument('-h','--ayuda',type=int,help='ayuda',action=argparse.BooleanOptionalAction)
args.add_argument('-sd','--subdom',help='parametro para buscar subdominios',action=argparse.BooleanOptionalAction)
args.add_argument('-hl','--hilos',help='hilos',type=int)
param= args.parse_args()