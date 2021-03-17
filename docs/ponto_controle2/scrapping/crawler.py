# Header
import requests
import re
from bs4 import BeautifulSoup
from gears import Usuario, BaseDados

# Set Stage

link_init = "https://pir2.forumeiros.com/memberlist"

members_page = requests.get(link_init)

user_page = ""
# Body

soup = BeautifulSoup(members_page.text, 'html.parser')
