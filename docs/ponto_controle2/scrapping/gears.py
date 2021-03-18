import mysql.connector
import re
import sys

class Usuario:
    def __init__(self):
        self.nome = ""
        self.sexo = '?'
        self.como_descobriu_forum = ""
        self.idade = 0
        self.localizacao = ""
        self.humor = ""
        self.emprego_lazer = ""
        self.nivel_instrucao = "Nenhum"
        self.data_inscricao = "01/12/1990"
        self.query = "undefined"

    def insert(self,object_database):
        self.query = "insert into USUARIO values ("+ "%s,"*8 +"%s)"
        self.tupla = (
            self.nome ,
            self.sexo ,
            self.como_descobriu_forum ,
            self.idade ,
            self.localizacao ,
            self.humor ,
            self.emprego_lazer ,
            self.nivel_instrucao ,
            self.data_inscricao
            )
        object_database.cursor.execute(self.query, self.tupla)

        object_database.con.commit()

    @property
    def data_inscricao(self):
        return self.__data_inscricao

    @data_inscricao.setter
    def data_inscricao(self,value): # dd/mm/aaaa  - > aaaa-mm-dd
        self.__data_inscricao = value[-4:] + '-' + value[3:5] + '-' + value[:2]

class BaseDados:
    def __init__(self):
        user = None
        password = None

        try:
            with open("credenciais.txt",'r') as arq:
                txt = arq.read()
                regex1 = r"banco\s+user:<([\w\d]+)>\s+password:<([\w\d]+)>"
                regex2 = r"banco\s+password:<([\w\d]+)>\s+user:<([\w\d]+)>"

                obj = re.match(regex1,txt)
                if obj:
                    (user,password) = obj.groups()

                obj = re.match(regex2,txt)
                if obj:
                    (password,user) = obj.groups()
        except FileNotFoundError:
            print("Arquivo de credenciais nao encontrado")
            sys.exit(1)

        if not ( user or password ):
            print("Erro ao obter as credenciais do banco, verifique o manual.")
            sys.exit(1)

        self.con = mysql.connector.connect(user=user,password=password,host='localhost',database='pir2')
        self.cursor = self.con.cursor()

def credenciais_forum():
    user = None
    password = None

    try:
        with open("credenciais.txt",'r') as arq:
            txt = arq.read()
            print(repr(txt))
            regex1 = r"forum\s+user:<([\w\d]+)>\s+password:<([\w\d]+)>"
            regex2 = r"forum\s+password:<([\w\d]+)>\s+user:<([\w\d]+)>"

            obj = re.match(regex1,txt)
            if obj:
                (user,password) = obj.groups()

            obj = re.match(regex2,txt)
            if obj:
                (password,user) = obj.groups()
    except FileNotFoundError:
        print("Arquivo de credenciais nao encontrado")
        sys.exit(1)

    if not ( user or password ):
        print("Erro ao obter as credenciais para acesso do forum, verifique o manual.")
        sys.exit(1)

    return (user,password)
