#Algoritmo para download de um arquivo .zip e extracao em uma pasta especificada

#Bibliotecas
import datetime, os, requests, StringIO, zipfile 
import pandas as pd

#Recebe o argumento "url" que possui o link de download e o "path" que recebe o caminho onde deseja extrair os dados do arquivo baixado
def downloadAndExtract(url, path):
    r = requests.get(url, stream='true')
    z = zipfile.ZipFile(StringIO.StringIO(r.content))
    z.extractall(path)

def putDateInPath(path):
    return path + datetime.date.today().strftime("%Y-%m-%d") + "/"

def dataframeMegaSenaToCsv(path):
	if not os.path.exists(path):
		os.makedirs(path)
	df_megasena.to_csv(path + "/nao_tratado_megasena.csv",sep=";", encoding="utf-8")

def dataframeQuinaToCsv(path):
	if not os.path.exists(path):
		os.makedirs(path)
	df_quina.to_csv(path + "/nao_tratado_quina.csv",sep=";", encoding="utf-8")

def getActualDate():
    return datetime.date.today().strftime("%Y-%m-%d")

print ("Baixando Arquivos... \n\n\n")
#Download Resultado MegaSena
downloadAndExtract('http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip', putDateInPath('./dados/MegaSena/'))

#Download Resultado Quina
downloadAndExtract('http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_quina.zip', putDateInPath('./dados/Quina/'))

print("Carregando Dataframes...\n\n\n")
#Carregando Arquivo em lista de Dataframe
list_megasena = pd.read_html("dados/Megasena/" + getActualDate() + "/D_MEGA.HTM")
list_quina = pd.read_html("dados/Quina/" + getActualDate() + "/D_QUINA.HTM")

#Concatenando lista de dataframes
df_megasena = pd.concat(list_megasena)
df_quina = pd.concat(list_quina)

print ("Salvando Arquivos CSV...\n\n\n")
#Salvando Resultado em .CSV
dataframeMegaSenaToCsv("planilha/MegaSena/" + getActualDate())
dataframeQuinaToCsv("planilha/Quina/" + getActualDate())

print ("Script Finalizado com sucesso:!!!")