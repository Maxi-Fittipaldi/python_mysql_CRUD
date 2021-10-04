import pymysql.cursors
from colorama import Fore 
class Connection():
    def __init__(self):
        self.cnn = pymysql.Connect(host='localhost',
                    user='root',
                    password='M@c4ord0fl4sh3r1x',
                    database='sql_testing',
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor)
        self.error = "Algo ocurrió, corrobora que hayas puesto bien los valores"
    
    def read(self):
        with self.cnn:
                with self.cnn.cursor() as cursor:
                    cursor.execute("SELECT * FROM products")
                    result = cursor.fetchall()
                    for x in result:
                        print(Fore.YELLOW + str(x))
    def create(self):
        try:
            p_id = int(input("product_id: "))
            name = input("name: ")
            q_in_stock = float(input("quantity_in_stock: "))
            unit_price = int(input("unit price: "))
            with self.cnn:
                    with self.cnn.cursor() as cursor:
                        result = cursor.execute("""
                        INSERT INTO products 
                        VALUES(%s,%s,%s,%s)""",(p_id, name, q_in_stock, unit_price))
                        self.cnn.commit()
        except:
            print(Fore.RED + self.error)
    def update(self):
        try:
            m_id = int(input("inserte el id del producto que quiere modificar: "))
            mName = input("name: ")
            mQ_in_stock = int(input("quantity_in_stock: "))
            mUnit_price =  float(input("unit price: "))
            with self.cnn:
                    with self.cnn.cursor() as cursor:
                        cursor.execute("""UPDATE products 
                        SET name = %s, 
                            quantity_in_stock = %s, 
                            unit_price = %s 
                        WHERE product_id = %s""",(mName, mQ_in_stock, mUnit_price,m_id))
                        self.cnn.commit()
        except:
            print(Fore.RED + self.error)

    def delete(self):
        d_id = int(input("inserte el id del producto que quiere eliminar: "))
        with self.cnn:
                with self.cnn.cursor() as cursor:
                    cursor.execute("DELETE FROM products WHERE product_id = %s",(d_id))
                    self.cnn.commit()

    def search(self):
        userSearch = input("Su búsqueda: ")
        with self.cnn:
                with self.cnn.cursor() as cursor:
                    cursor.execute(f'SELECT * FROM products WHERE name LIKE "%{userSearch}%"')
                    result = cursor.fetchall()
                    for x in result:
                        print(Fore.YELLOW + str(x))
