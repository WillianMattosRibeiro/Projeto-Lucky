# Created By Willian Mattos Ribeiro - Blueshift #
#				Source to Raw					#

# Bibliotecas
import datetime, os, requests

# Argumentos #
link_megasena = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
file_path = '/raw/MegaSena/'

def downloadFile(url):
	try:
		r = requests.get(url, stream='true')
		return r
	except Exception, e:
		print "### Download Error! ###\nDetails:\n " + e.message 
		raise

def putFileInPath(f, path):
	# Concatenando diretorio completo com data
	fileName = getDate() + "-megasena.zip"
	fullPath = os.getcwd() + path + getDate() + "\\"

	if not os.path.exists(fullPath):
		os.makedirs(fullPath)

	try:
		open(fullPath + fileName, 'wb').write(f.content)
	except Exception, e:
		print "### Save File Error! ###\nDetails:\n " + e.message
		raise e

def getDate():
    return datetime.date.today().strftime("%Y-%m-%d")

print ("# Baixando Arquivos... \n\n")
f = downloadFile(link_megasena)

print ("# Salvando Arquivos No diretorio... \n\n")
putFileInPath(f, file_path)

print ("# Script Finalizado com sucesso:!!!")