import pandas as pd
import urllib

def loadFile(url):
	return urllib.urlopen(url).read()

html_string = loadFile("dados/2018-01-02/D_MEGA.HTM")
data = pd.read_html(html_string, header=0) # Parse the HTML as a string
arquivo = open("tratado.csv", "w")

arquivo.write(html_string)