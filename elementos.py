from colorama import Fore
from threading import Lock

lock = Lock()
encontrado = []

data = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

logo = Fore.GREEN+r'''
 __          __  _     _____             _             
 \ \        / / | |   |  __ \           | |            
  \ \  /\  / /__| |__ | |__) |__ _ _ __ | |_ ___  _ __ 
   \ \/  \/ / _ \ '_ \|  _  // _` | '_ \| __/ _ \| '__|
    \  /\  /  __/ |_) | | \ \ (_| | |_) | || (_) | |   
     \/  \/ \___|_.__/|_|  \_\__,_| .__/ \__\___/|_|   
                                  | |                  
                                  |_|                  
 
Por Urb@n

'''

