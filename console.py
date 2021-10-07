import os
from colorama import Fore
from Connection import db
from index import options
import time

# START console
class Console():

    def main(self):
        db.__init__()
        print(Fore.MAGENTA + "write the action you want to execute ('help' to see all the functions): ")
        action = input(">> ")
        match = 0
        for i in options.navigate(["main","content"]):
            if action == i:
                match += 1
                self.clear()
                options.navigate(["main","content",action,"function"])()
        if match == 0:
            self.clear()
            print(Fore.RED + "the function you are typing does not exist")
        self.main() #en loop

    def help(self):
        for i in options.navigate(["main","content"]):
            print(Fore.GREEN + f"- {i}")
            print(Fore.YELLOW + "_______________")

    def clear(self):
        os.system("cls") #windows
        os.system("clear") #linux

    def quit_program(self):
        print(Fore.RED + "Program closed")
        time.sleep(1)
        self.clear()
        time.sleep(1)
        quit() #python function
# END console
console = Console()