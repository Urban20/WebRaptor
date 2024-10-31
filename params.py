import argparse


args = argparse.ArgumentParser(
    prog='fuzzing web',
    usage='''fuzzing [url] [dic]
    -h o --help para desplegar la ayuda ''',

    description= 'creado por urb@n para descubrir rutas ocultas en paginas web'
    )

args.add_argument('url',type=str,help='url de la web a hacer fuzzing')
args.add_argument('dic',type=str,help='diccionario en formato .txt que se utiliza para hacer fuzzing, debe estar escrito en formato de listado')
args.add_argument('-g','--guardar',help='argumento opcional para guardar las urls en caso de encontrarse alguna',action=argparse.BooleanOptionalAction)
args.add_argument('-l','--lineal',action=argparse.BooleanOptionalAction,help='argumento opcional para la busqueda de directorios de forma lineal (consume menos recursos del cpu)')

param= args.parse_args()