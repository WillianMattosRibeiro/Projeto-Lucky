#Bibliotecas
import urllib
import pandas as pd
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("dados/2018-01-02/D_MEGA.HTM", "r"), 'lxml') # Parse the HTML as a string
#table = soup.find_all('table')[0] # Pegar a primeira tabela
header = soup.find_all('tr')[0] # Pegar a primeira linha (Cabecalho)

cabecalho = pd.DataFrame(columns=range(0,20), index = [0]) # range(<indice_da_primeira_coluna>,<indice_da_ultima_coluna>)

row_marker = 0
for row in header.find_all('th'):
	column_marker = 0
	columns = row.find_all('small')
	for column in columns:
		cabecalho[row_marker,column_marker] = column.get_text()
		column_marker += 1
	row_marker += 1

#matriz = [[column.get_text() for column in row.find_all('small')] for row in header.find_all('th')]

#print [[column.get_text() for column in row.find_all('small')] for row in header.find_all('th')]
