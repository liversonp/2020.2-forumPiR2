# Header
import requests
import mysql.connector
import re
import sys
from bs4 import BeautifulSoup

# Set Stage
user = None
password = None

try:
    with open("credenciais.txt",'r') as arq:
        txt = arq.read()
        regex1 = r"user:<(\S+)>\s+?password:<(\S+)>\s*?"
        regex2 = r"password:<(\S+)>\s+?user:<(\S+)>\s*?"

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
    print("Erro ao obter as credenciais, verifique o manual.")
    sys.exit(1)

database = mysql.connector.connect(user=user,password=password,host='localhost',database='pir2')

html_init = "https://pir2.forumeiros.com/memberlist"

actual_page = requests.get(html_init)

# Body
