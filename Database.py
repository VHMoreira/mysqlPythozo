import pymysql
from Jogo import Jogo


class Database:

    def update(self,table,where):
        aux=['name','nota','informacao']
        db = pymysql.connect("db4free.net", "alvarozao", "fe7924d3", "testesbancao5")
        cursor = db.cursor()
        try:
            for i in range(0,len(aux)):
                sql = 'UPDATE Jogos SET {} = "{}" WHERE id = {}'.format(aux[i],table[i],where)
                print(sql)
                cursor.execute(sql)
            db.commit()
            db.close()
        except:
            db.rollback()

    def readTabela(self):
        db = pymysql.connect("db4free.net","alvarozao","fe7924d3","testesbancao5")
        cursor = db.cursor()

        sql = """SELECT * FROM Jogos;"""
        listaJogos = []
        try:
            cursor.execute(sql)
            resultado = cursor.fetchall()
            i = 0
            for linha in resultado:
                i += 1
                nome = linha[0]
                nota = linha[1]
                idd = linha[2]
                src = linha[3]
                info = linha[4]
                listaJogos.append(Jogo(nome,nota,idd,src,info))
            db.close()
            return listaJogos
        except:
            print("Lista vazia")
            db.close()
            return listaJogos



    def insertInto(self,table):
        db = pymysql.connect("db4free.net", "alvarozao", "fe7924d3", "testesbancao5")
        cursor = db.cursor()
        try:
            cursor.execute('INSERT INTO Jogos VALUES ("{}","{}","{}","{}","{}")'.format(table[0],table[1],table[2],table[3],table[4]))
            db.commit()
            db.close()
            print("inseriu no bd")
        except:
            db.rollback()
            print("ERRO NA INSERÇÃO")

    def remove(self,where):
        print(where)
        db = pymysql.connect("db4free.net", "alvarozao", "fe7924d3", "testesbancao5")
        cursor = db.cursor()
        try:
            cursor.execute('DELETE FROM Jogos WHERE id = {};'.format(where))
            db.commit()
            db.close()
            print("REMOVEU {} DO BANCO DE DADOS".format(where))
        except:
            print("ERRO NA REMOÇÃO")
            db.rollback()

    def criarTabela(self):
        db = pymysql.connect("db4free.net", "alvarozao", "fe7924d3", "testesbancao5")
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Jogos (
        name CHAR(30),
        nota INT,
        id CHAR(50),
        srcImage CHAR(100),
        informacao CHAR(200)
        );""")  #deleta tabela sempre que executado
    
        db.close()
