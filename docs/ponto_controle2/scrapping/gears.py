import mysql.connector
import re
import sys
from bs4 import BeautifulSoup

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
        self.link_root = "https://pir2.forumeiros.com"

    def hunt_data(self,line_object,session_object):
        # Acessando pagina do usuario
        link_usr_page = line_object.find_all("td",{"class":"avatar-mini"})[0].find('a').get('href')
        link_usr_page = self.link_root + link_usr_page
        raw_page_user = session_object.post(link_usr_page)
        soup = BeautifulSoup(raw_page_user.text,'html.parser')
        # Extraindo informacoes
        self.nome = line_object.find("td",{"class":"avatar-mini"}).find('a').text
        atributos = soup.find("div",{"id":"profile-tab-field-profil"})

        try:
            self.como_descobriu_forum = atributos.find("dl",{"id":"field_id2"}).find("dd").find("div").text
        except:
            pass
        try:
            self.idade = int(atributos.find("dl",{"id":"field_id-5"}).find("dd").find("div").text)
        except:
            pass
        try:
            self.localizacao = atributos.find("dl",{"id":"field_id-11"}).find("dd").find("div").text
        except:
            pass
        try:
            self.humor = atributos.find("dl",{"id":"field_id-8"}).find("dd").find("div").text
        except:
            pass
        try:
            self.emprego_lazer = atributos.find("dl",{"id":"field_id-9"}).find("dd").find("div").text
        except:
            pass
        try:
            self.nivel_instrucao = atributos.find("dl",{"id":"field_id1"}).find("dd").find("div").text
        except:
            pass
        try:
            self.data_inscricao = atributos.find("dl",{"id":"field_id-4"}).find("dd").find("div").text
        except:
            pass
        try:
            self.sexo = atributos.find("dl",{"id":"field_id-7"}).find("dd").find("div",{"class":"field_uneditable"}).find('img')['alt'][:1]
        except:
            pass

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
            with open("credenciais_bd.txt",'r') as arq:
                txt = arq.read()
                regex1 = r"\s*user:<([\S]+)>\s+password:<([\S]+)>"
                regex2 = r"\s*password:<([\S]+)>\s+user:<([\S]+)>"

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
        with open("credenciais_forum.txt",'r') as arq:
            txt = arq.read()
            regex1 = r"\s*user:<([\S]+)>\s+password:<([\S]+)>"
            regex2 = r"\s*password:<([\S]+)>\s+user:<([\S]+)>"

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
