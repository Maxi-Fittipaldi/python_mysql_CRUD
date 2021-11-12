from os import error
import pymysql.cursors
from colorama import Fore 
class Connection():
    def __init__(self):
        self.cnn = pymysql.Connect(host='localhost',
                    user='root',
                    password='',
                    database='sql_testing',
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor)
    
    def read(self,query):
        with self.cnn:
                with self.cnn.cursor() as cursor:
                    cursor.execute(query)
                    return cursor.fetchall()
                    
    def manipulate(self,query, params = ()): #insert, update, delete
        with self.cnn:
                with self.cnn.cursor() as cursor:
                    result = cursor.execute(query,params)
                    self.cnn.commit()
    def easyproc(self, proc, params = ()): #procedures with params
        with self.cnn:
            with self.cnn.cursor() as cursor:
                result = cursor.callproc(proc,params)
                self.cnn.commit()
                    
db = Connection()