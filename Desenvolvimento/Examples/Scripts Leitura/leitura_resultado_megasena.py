#Algoritmo para ler o conteudo de um .HTM e filtrar por coluna

#Bibliotecas
import urllib
import pandas as pd
from bs4 import BeautifulSoup

def loadFile(url):
	return urllib.urlopen(url).read()

html_string = loadFile("dados/2018-01-02/D_MEGA.HTM")

soup = BeautifulSoup(html_string, 'lxml') # Parse the HTML as a string

table = soup.find_all('table')[0] # Grab the first table

new_table = pd.DataFrame(columns=range(0,21), index = [0]) # range(<indice_da_primeira_coluna>,<indice_da_ultima_coluna>)

row_marker = 0
for row in table.find_all('tr'):
	column_marker = 0
	columns = row.find_all('td')
	for column in columns:
		new_table.append[row_marker,column_marker] = column.get_text()
		column_marker += 1
	#row_marker += 1
#new_table.to_csv("tratado.csv", sep='|', encoding='utf-8')

print new_table