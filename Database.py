import pymysql

class Database:
    def __init__(self, hostname,admin,password,database_name):
        self.db = pymysql.connect(hostname,admin,password,database_name)
        self.cursor = db.cursor()

    def update(self):
        pass

    def alterTable(self):
        pass

    def insertInto(self):
        pass

    def remove(self):
        pass