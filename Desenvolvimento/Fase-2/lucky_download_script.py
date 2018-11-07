#Download Script

#Bibliotecas
import datetime, os, requests

#Recebe o argumento "url" que possui o link de download e o "path" que recebe o caminho onde deseja extrair os dados do arquivo baixado
def downloadAndExtract(url, path):
    r = requests.get(url, stream='true')

def putDateInPath(path):
    return path + datetime.date.today().strftime("%Y-%m-%d") + "/"

def getActualDate():
    return datetime.date.today().strftime("%Y-%m-%d")

print ("# Baixando Arquivos... \n\n")
#Download Resultado MegaSena
downloadAndExtract('http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip', putDateInPath(os.getcwd() + '/download/raw/MegaSena/'))

print ("# Script Finalizado com sucesso:!!!")