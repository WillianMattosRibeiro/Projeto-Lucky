# Created By Willian Mattos Ribeiro - Blueshift #
#				Raw to Swamp Script				#

# Bibliotecas
import datetime, os

# Argumentos #
link_megasena = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
file_path = '/raw/MegaSena/'

def downloadAndExtract(url, path):
    r = requests.get(url, stream='true')
    z = zipfile.ZipFile(StringIO.StringIO(r.content))
    z.extractall(path)

print ("# Carregando Arquivos... \n\n")