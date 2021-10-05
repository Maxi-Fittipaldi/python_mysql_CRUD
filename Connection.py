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
    
    def read(self,query):
        with self.cnn:
                with self.cnn.cursor() as cursor:
                    cursor.execute(query)
                    return cursor.fetchall()
                    
    def manipulate(self,query, params = ()): #insert, update, delete
        try:
            with self.cnn:
                    with self.cnn.cursor() as cursor:
                        result = cursor.execute(query,params)
                        self.cnn.commit()
        except:
            return self.error
                    
