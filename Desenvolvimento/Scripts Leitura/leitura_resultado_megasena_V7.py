import pandas as pd
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("dados/2018-01-02/D_MEGA.HTM","r"), 'lxml')

dados = ""

for row in soup.find_all('tr'):
	columns = row.find_all('td')
	for column in columns:
		dados += column.get_text()

arquivo = open("tratado.csv", "w")

arquivo.write(dados)