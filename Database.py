import pymysql
from Jogo import Jogo


class Database:
    def __init__(self):
        pass

    def update(self,table,where,new):
        pass

    def readTabela(self):
        db = pymysql.connect("db4free.net","alvarozao","fe7924d3","testesbancao5")
        cursor = db.cursor()

        sql = """SELECT * FROM Jogo"""
        listaJogos = []
        try:
            cursor.execute(sql)
            print(sql)
            resultado = cursor.fetchall()
            i = 0
            for linha in resultado:
                print("lendo")
                print(i)
                i += 1
                nome = linha[0]
                nota = linha[1]
                id = linha[2]
                src = linha[3]
                info = linha[4]
                listaJogos.append(Jogo(nome,nota,id,src,info))
            db.close()
            return listaJogos
        except:
            print("Lista vazia")
            db.close()
            return listaJogos



    def insertInto(self,table):
        db = pymysql.connect("db4free.net", "alvarozao", "fe7924d3", "testesbancao5")
        cursor = db.cursor()

        sql = """INSERT INTO Jogo(name, nota, index, srcImage, informacao)
         VALUES ('{0}',{1},{2},'{3}','{4}')""".format(table[0],table[1],table[2],table[3],table[4])
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            db.close()
            print("inseriu no bd")
        except:
            print("Erro na insercao")
            db.rollback()
            db.close()

    def remove(self,table,where):
        pass

    def criarTabela(self):
        db = pymysql.connect("db4free.net", "alvarozao", "fe7924d3", "testesbancao5")
        cursor = db.cursor()

        cursor.execute("DROP TABLE IF EXISTS Jogo")  #deleta tabela sempre que executado
        sql = """CREATE TABLE Jogo (
        name CHAR(30),
        nota INT,
        id INT NOT NULL,
        srcImage CHAR(100),
        informacao CHAR(200)
        )"""
        cursor.execute(sql)
        db.close()
