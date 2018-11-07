#Bibliotecas
import datetime, os, StringIO 
import pandas as pd
import numpy as np

def is_nan(x):
    return (x is np.nan or x != x)

def getActualDate():
    return datetime.date.today().strftime("%Y-%m-%d")

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass
	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass
	return False    

#Carregando arquivo no DataFrame
df_nao_tratado = pd.read_csv("planilha/Megasena/" + getActualDate() + "/nao_tratado_megasena.csv", sep=';')

#Imprimir apartir do n-esimo numero...
n = 3

#Imprimir N numeros, tal que N = qtd
qtd = 1

index_last_df = 2

for i in range(n-1, n+qtd):
	if is_nan(df_nao_tratado.loc[i]['Concurso']) or is_number(df_nao_tratado.loc[i]['Concurso']) == False:
		df_nao_tratado[index_last_df]['UF'].concat()("," + str(df_nao_tratado.loc[i]['Data Sorteio']))
		df_nao_tratado.drop([i])
	else:
		index_last_df = i
	print df_nao_tratado.loc[i]

'''
print "Concurso: ", df_nao_tratado.loc[index_last_df]['Concurso']
print "Linha: ", index_last_df
print df_nao_tratado.loc[index_last_df]['Cidade']
print df_nao_tratado.loc[index_last_df]['UF']

print "\n"

print "Concurso: ", df_nao_tratado.loc[index_last_df+1]['Concurso']
print "Linha: ", index_last_df+1
print df_nao_tratado.loc[index_last_df+1]['Concurso']
print df_nao_tratado.loc[index_last_df+1]['Data Sorteio']

print "\nConcatenado:\n"
print str(df_nao_tratado.loc[index_last_df]['Cidade']) + "," + str(df_nao_tratado.loc[index_last_df+1]['Concurso'])
print df_nao_tratado.loc[index_last_df]['UF'] + "," + str(df_nao_tratado.loc[index_last_df+1]['Data Sorteio'])
'''