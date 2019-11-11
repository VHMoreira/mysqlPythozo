import pymysql

class Database:
    def __init__(self, hostname,admin,password,database_name):
        self.db = pymysql.connect(hostname,admin,password,database_name)
        self.cursor = self.db.cursor()

    def update(self,table,where,new):
        pass

    def read(self,table,where):
        pass

    def insertInto(self,table,columns=[],values=[]):
        pass

    def remove(self,table,where):
        pass