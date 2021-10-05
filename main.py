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
    print(Fore.MAGENTA + "write the action you want to execute ('help' to see all the functions): ")
    action = input(">> ")
    match = 0
    for i in options:
        if action == i:
            match += 1
            clear()
            options.get(action)()
    if match == 0:
        clear()
        print(Fore.RED + "the function you are typing does not exist")
    main() #en loop

main()