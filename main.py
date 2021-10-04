from toFrontEnd import *

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