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
db = Connection()

# START CRUD
# START basic 
def create():
    p_id = int(input("product_id: "))
    name = input("name: ")
    q_in_stock = int(input("quantity_in_stock: "))
    unit_price = float(input("unit price: "))
    db.manipulate("""INSERT INTO products 
    VALUES(%s,%s,%s,%s)""",(p_id, name, q_in_stock, unit_price))

def read():
    result = db.read("SELECT * FROM products")
    for x in result:
        print(Fore.YELLOW + str(x))

def update():
    m_id = int(input("write the product id you want to modify: "))
    mName = input("name: ")
    mQ_in_stock = int(input("quantity_in_stock: "))
    mUnit_price =  float(input("unit price: "))
    db.manipulate("""UPDATE products 
    SET name = %s, 
        quantity_in_stock = %s, 
        unit_price = %s 
    WHERE product_id = %s""",(mName, mQ_in_stock, mUnit_price,m_id))

def delete():
    d_id = int(input("write the product id you want to delete: "))
    db.manipulate("DELETE FROM products WHERE product_id = %s",(d_id))
# END basic

#START extra
def search():
    userSearch = input("Search: ")
    result = db.read(f"SELECT * FROM products WHERE name LIKE '%{userSearch}%'")
    for x in result:
        print(Fore.YELLOW + str(x))

def custom():
    print(Fore.LIGHTMAGENTA_EX + "manipulate or read?: ")
    mode = input(">>")
    
    if mode == "manipulate":
        print(Fore.LIGHTGREEN_EX + "manipulate mode")
        query = input(">>")
        print(query)
        db.manipulate(query)
    elif mode == "read":
        print(Fore.LIGHTGREEN_EX + "read mode")
        query = input(">>")
        result = db.read(query)
        for x in result:
            print(Fore.LIGHTYELLOW_EX + str(x))
    elif mode == "quit":
        quit_program()
    else:  
        print(Fore.RED + "La opción no es válida")
        custom()
        

#END extra
#END CRUD

# START sys

def help():
    for i in options:
        print(Fore.GREEN + f"- {i}")
        print(Fore.YELLOW + "_______________")

def clear():
    os.system("cls") #windows
    os.system("clear") #linux

def quit_program():
    print(Fore.RED + "Program closed")
    time.sleep(1)
    clear()
    time.sleep(1)
    quit() #python function

# END sys

#index
options = { 
    "create": create,
    "read": read,
    "update": update,
    "delete": delete,
    "search": search,
    "help": help,
    "quit": quit_program,
    "custom": custom
}