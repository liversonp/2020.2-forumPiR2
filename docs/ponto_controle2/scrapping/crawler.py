# Header
import requests
import re
from bs4 import BeautifulSoup
from gears import Usuario, BaseDados, credenciais_forum
import sys

# Login into the forum
(user_login,password_login) = credenciais_forum()
banco = BaseDados()

link_login = "https://pir2.forumeiros.com/login"

login_data = {"login":"Conectar-se", "username": user_login, "password": password_login,}#"persistent":'1' }

with requests.session() as s:
    ans = s.post(link_login,data=login_data)
    link_members = "https://pir2.forumeiros.com/memberlist"
    rawListMembers = s.post(link_members)
    print(rawListMembers.text)
