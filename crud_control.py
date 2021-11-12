from control import *
#colorama
import colorama
from colorama import Fore
#exceptions
from exceptions import *
#connection
from Connection import db
colorama.init(autoreset=True)

class Crud_control(object):
    def create(id, name,q_in_stock, unit_price):
        try:
            id = int(id)
            q_in_stock = int(q_in_stock)
            unit_price = float(unit_price)
            result = db.read("SELECT product_id FROM products")
            db.__init__()
            used_id = lookForIn(id, result, "product_id")
            valid_name = Validate.bySmallerLen(name,40)
            valid_uprice = Validate.simpleIf.smallerThan(unit_price,9.99)
            if used_id == False:
                if valid_name == True and valid_uprice == True:
                    print(Fore.GREEN + "Transaction commited")
                    return True
                else:
                    raise InvalidData
            else:
                raise UsedId
        except InvalidData:
            print(Fore.RED + "Transaction denied, invalid data")
        except UsedId:
            print(Fore.RED + "Transaction denied, the id you are typing already exists, try with another number")
        except: 
            print(Fore.RED + "Transaction denied, invalid data")
    def update(id, name,q_in_stock, unit_price):
        try:
            id = int(id)
            q_in_stock = int(q_in_stock)
            unit_price = float(unit_price)
            result = db.read("SELECT product_id FROM products")
            db.__init__()
            used_id = lookForIn(id, result, "product_id")
            valid_name = Validate.bySmallerLen(name,40)
            valid_uprice = Validate.simpleIf.smallerThan(unit_price,9.99)
            if used_id == True:
                if valid_name == True and valid_uprice == True:
                    print(Fore.GREEN + "Transaction commited")
                    return True
                else:
                    raise InvalidData
            else:
                raise UsedId
        except InvalidData:
            print(Fore.RED + "Transaction denied, invalid data")
        except UsedId:
            print(Fore.RED + "Transaction denied, the id you are typing does not exist")
        except: 
            print(Fore.RED + "Transaction denied, invalid data")
    def delete(id):
        try:
            id = int(id)
            result = db.read("SELECT product_id FROM products")
            db.__init__()
            used_id = lookForIn(id, result, "product_id")
            if used_id == True:
                print(Fore.GREEN + "Transaction commited, a register was deleted")
                return True
            else:
                raise UsedId
        except UsedId:
            print(Fore.RED + "Transaction denied, the register does not exist")
        except:
            print(Fore.RED + "Transaction denied, invalid data")
