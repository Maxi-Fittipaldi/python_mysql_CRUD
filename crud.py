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
#control and validation
from control import *
from crud_control import Crud_control
#console
from console import console
colorama.init(autoreset=True)


# START CRUD
# START basic 
class CRUD():

    def create(self): 
            p_id = input("product_id: ")
            name = input("name: ")
            q_in_stock = input("quantity_in_stock: ")
            unit_price = input("unit price: ")
            isValid = Crud_control.create(p_id, name, q_in_stock, unit_price)
            if isValid == True:
                db.manipulate("""INSERT INTO products 
                VALUES(%s,%s,%s,%s)""",(p_id, name, q_in_stock, unit_price))


    def read(self):
        result = db.read("SELECT * FROM products")
        for x in result:
            print(Fore.YELLOW + str(x))


    def update(self):
            m_id = input("write the product id you want to modify: ")
            mName = input("name: ")
            mQ_in_stock = input("quantity_in_stock: ")
            mUnit_price =  input("unit price: ")

            isValid = Crud_control.update(m_id, mName, mQ_in_stock, mUnit_price)
            if isValid == True:
                db.manipulate("""UPDATE products 
                SET name = %s, 
                    quantity_in_stock = %s, 
                    unit_price = %s 
                WHERE product_id = %s""",(mName, mQ_in_stock, mUnit_price,m_id))
    def delete(self):
            d_id = input("write the product id you want to delete: ") 
            isValid = Crud_control.delete(d_id)
            if isValid:
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
        console.clear()        
        options.navigate(["main","content"])


#END CRUD

crud = CRUD()
adv = Advanced()
custom = Custom()
