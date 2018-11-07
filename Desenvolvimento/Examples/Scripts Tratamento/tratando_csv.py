#Bibliotecas
import datetime, os, StringIO 
import pandas as pd

def getActualDate():
    return datetime.date.today().strftime("%Y-%m-%d")

df_nao_tratado = pd.read_csv("planilha/Megasena/" + getActualDate() + "/nao_tratado_megasena.csv")
print df_nao_tratado