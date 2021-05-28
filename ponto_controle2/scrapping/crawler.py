# Header
import requests
import re
from bs4 import BeautifulSoup
from gears import Usuario, BaseDados, credenciais_forum
import sys

# Login into the forum
(user_login,password_login) = credenciais_forum()
banco = BaseDados()

link_root = "https://pir2.forumeiros.com"
link_login = link_root + "/login"
link_members = link_root + "/memberlist"

login_data = {"login":"Conectar-se", "username": user_login, "password": password_login,}

user = Usuario()

# modo == 1, adiciona no banco de dados
# modo == 2, adiciona no csv
# modo == 3, adiciona no csv e no banco de dados
modo = 2
if modo  > 1:
    user.init_csv()

with requests.session() as s:
    ans = s.post(link_login,data=login_data)
    next_page = link_members
    i = 1
    while True:
        print("Pagina {}".format(i))
        rawListMembers = s.get(next_page)

        soup = BeautifulSoup(rawListMembers.text, 'html.parser')
        tr = soup.findAll("tr", {"class": "row1"}) + soup.findAll("tr", {"class": "row2"})

        for raw_u in tr:
            user = Usuario()
            user.hunt_data(raw_u,s)
            if modo == 3:
                user.insert(banco)
                user.make_csv()
            elif modo == 2:
                user.make_csv()
            elif modo == 1:
                user.insert(banco)
            #break


        next_page = link_members + "?mode=lastvisit&order=DESC&start={}&username".format(i*50)
    print("Fim")

banco.con.close()
