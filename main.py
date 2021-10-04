#funciones de consola
import os
#time
import time
#conexión
from Connection import Connection
#colorama
import colorama
from colorama import Fore

colorama.init(autoreset=True)
#llamada a la clase
db = Connection()
#funciones locales
def help():
    for i in options:
        print(Fore.GREEN + f"- {i}")
        print(Fore.YELLOW + "_______________")

def clear():
    os.system("cls") #windows
    os.system("clear") #linux

def salir():
    print(Fore.RED + "Has salido del programa")
    time.sleep(1)
    clear()
    time.sleep(1)
    quit() #función reservada de de python


#índice
options = { 
    "create": db.create,
    "read": db.read,
    "update": db.update,
    "delete": db.delete,
    "search": db.search,
    "help": help,
    "quit": salir
}
print(Fore.LIGHTCYAN_EX + """
 ██████╗██████╗ ██╗   ██╗██████╗ 
██╔════╝██╔══██╗██║   ██║██╔══██╗
██║     ██████╔╝██║   ██║██║  ██║
██║     ██╔══██╗██║   ██║██║  ██║
╚██████╗██║  ██║╚██████╔╝██████╔╝
 ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
""")

def main():
    db.__init__()
    print(Fore.MAGENTA + "Especifique la acción que quiere ejecutar ('help' para ver funciones): ")
    action = input(">> ")
    match = 0
    for i in options:
        if action == i:
            match += 1
            clear()
            options.get(action)()
    if match == 0:
        clear()
        print(Fore.RED + "no se ha encontrado la función")
    main() #en loop

main()