import requests, bs4
from datetime import datetime

year = str(datetime.now().year)
month = str(datetime.now().month).zfill(2)
day = str(datetime.now().day).zfill(2)
url = 'http://catedral.prefeitura.unicamp.br/cardapio.php?d=' + year + '-' + month + '-' day

# The variable 'res' will store the page's content
res = requests.get(url)

# Raise exception if http error occurs
res.raise_for_status()

# Create a BeautifulSoup object, using lxml as parser
bsobject = bs4.BeautifulSoup(res.text, 'lxml')

# Take the menu
menu = bsobject.select('#sistema_cardapio > table tr td')


# Getting each menu entry
lunch = menu[9].getText().split(':')[1].title()
veggie_lunch = menu[18].getText().split(':')[1].title()
dinner = menu[27].getText().split(':')[1].title()
veggie_dinner = menu[36].getText().split(':')[1].title()

# Print the menu main meals
print("Almoço: " + lunch)
print("Almoço vegetariano: " + veggie_lunch)
print("Jantar: " + dinner)
print("Jantar vegetariano: " + veggie_dinner)