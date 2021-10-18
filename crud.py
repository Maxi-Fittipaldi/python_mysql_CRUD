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
#console
from console import console
colorama.init(autoreset=True)


# START CRUD
# START basic 
class CRUD():

    def create(self):
        try:
            p_id = int(input("product_id: "))
            name = input("name: ")
            q_in_stock = int(input("quantity_in_stock: "))
            unit_price = float(input("unit price: "))
            db.manipulate("""INSERT INTO products 
            VALUES(%s,%s,%s,%s)""",(p_id, name, q_in_stock, unit_price))
        except:
            print(Fore.RED + "Something went wrong, check the input")


    def read(self):
        result = db.read("SELECT * FROM products")
        for x in result:
            print(Fore.YELLOW + str(x))


    def update(self):
        try:
            m_id = int(input("write the product id you want to modify: "))
            result = db.read("SELECT product_id FROM products")
            db.__init__()
            valid_id = lookForIn(m_id,result,"product_id")
            if valid_id:
                
                mName = input("name: ")
                mQ_in_stock = int(input("quantity_in_stock: "))
                mUnit_price =  float(input("unit price: "))
                db.manipulate("""UPDATE products 
                SET name = %s, 
                    quantity_in_stock = %s, 
                    unit_price = %s 
                WHERE product_id = %s""",(mName, mQ_in_stock, mUnit_price,m_id))
            else:
                raise ValueError
        except:
            print(Fore.RED + "Something went wrong, check the input")
    def delete(self):
        try:
            d_id = int(input("write the product id you want to delete: ")) 
            result = db.read("SELECT product_id FROM products")
            db.__init__()
            valid_id = lookForIn(d_id,result,"product_id")
            if valid_id:
                db.manipulate("DELETE FROM products WHERE product_id = %s",(d_id))
            else:
                raise ValueError
        except: 
            print(Fore.RED + "Something went wrong, check the input")
            
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

#END advanced
#START misc
def lookForIn(param, data,key = None):
    if key == None: 
        for x in data:
            if x == param:
                return True
    else:
        for x in data:
            if x[key] == param:
                return True
    return False

#END misc
#END CRUD

crud = CRUD()
adv = Advanced()
custom = Custom()