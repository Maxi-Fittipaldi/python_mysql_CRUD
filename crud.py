#funciones de consola
import os
#time
import time
#conexión
from Connection import db
#colorama
import colorama
from colorama import Fore
#options
from Tree import options

colorama.init(autoreset=True)


# START CRUD
# START basic 
class CRUD():

    def create(self):
        p_id = int(input("product_id: "))
        name = input("name: ")
        q_in_stock = int(input("quantity_in_stock: "))
        unit_price = float(input("unit price: "))
        db.manipulate("""INSERT INTO products 
        VALUES(%s,%s,%s,%s)""",(p_id, name, q_in_stock, unit_price))

    def read(self):
        result = db.read("SELECT * FROM products")
        for x in result:
            print(Fore.YELLOW + str(x))

    def update(self):
        m_id = int(input("write the product id you want to modify: "))
        mName = input("name: ")
        mQ_in_stock = int(input("quantity_in_stock: "))
        mUnit_price =  float(input("unit price: "))
        db.manipulate("""UPDATE products 
        SET name = %s, 
            quantity_in_stock = %s, 
            unit_price = %s 
        WHERE product_id = %s""",(mName, mQ_in_stock, mUnit_price,m_id))

    def delete(self):
        d_id = int(input("write the product id you want to delete: "))
        db.manipulate("DELETE FROM products WHERE product_id = %s",(d_id))
# END basic

#START advanced
class Advanced():

    def search(self):
        userSearch = input("Search: ")
        result = db.read(f"SELECT * FROM products WHERE name LIKE '%{userSearch}%'")
        for x in result:
            print(Fore.YELLOW + str(x))

    def custom(self):
        print(Fore.LIGHTMAGENTA_EX + "manipulate or read?: ")
        mode = input(">>")
        options.navigate(["main","content","custom","content",mode,"function"])()

class Custom():
    def manipulate(self):
        print(Fore.LIGHTGREEN_EX + "manipulate mode")
        query = input(">>")
        print(query)
        db.manipulate(query)

    def read(self):
        print(Fore.LIGHTGREEN_EX + "read mode")
        query = input(">>")
        result = db.read(query)
        for x in result:
            print(Fore.LIGHTYELLOW_EX + str(x))
    def go_back(self):
        options.navigate(["main","content"])

#END advanced
#END CRUD

crud = CRUD()
adv = Advanced()
custom = Custom()