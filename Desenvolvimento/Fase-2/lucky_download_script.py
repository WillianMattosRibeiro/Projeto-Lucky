#Download Script

#Bibliotecas
import datetime, os, requests, zipfile, StringIO

# Argumentos #
link_megasena = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
file_path = '/download/MegaSena/'

def downloadFile(url):
    r = requests.get(url, stream='true')
    return r

def putFileInPath(f, path):
	# Concatenando diretorio completo com data
    fullPath = os.getcwd() + path + getDate()
    
    if not os.path.exists(fullPath):
		os.makedirs(fullPath)

    open(fullPath + "/megasena.zip", 'wb').write(f.content)

def getDate():
    return datetime.date.today().strftime("%Y-%m-%d")

print ("# Baixando Arquivos... \n\n")
try:
	f = downloadFile(link_megasena)
except Exception, e:
	e = sys.exc_info()[0]
else:
	print ("# Falha ao efetuar o download do arquivo... \n\n")

print ("# Salvando Arquivos No diretorio... \n\n")
try:
	putFileInPath(f, file_path)
except Exception, e:
	e = sys.exc_info()[0]
else:
	print ("# Falha ao salvar o arquivo \n\n")

print ("# Script Finalizado com sucesso:!!!")