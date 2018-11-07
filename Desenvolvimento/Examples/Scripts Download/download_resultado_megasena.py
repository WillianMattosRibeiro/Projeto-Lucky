#Algoritmo para download de um arquivo .zip e extracao em uma pasta especificada

#Bibliotecas
import requests, zipfile, StringIO, datetime
import pandas as pd

#Recebe o argumento "url" que possui o link de download e o "path" que recebe o caminho onde deseja extrair os dados do arquivo baixado
def downloadAndExtract(url, path):
	r = requests.get(url, stream='true')
	z = zipfile.ZipFile(StringIO.StringIO(r.content))
	z.extractall(path)

def putDateInPath(path):
	return path + datetime.date.today().strftime("%Y-%m-%d") + "/"

downloadAndExtract('http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip', putDateInPath('./dados/'))