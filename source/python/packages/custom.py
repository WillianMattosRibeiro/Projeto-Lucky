# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

#Bibliotecas
import datetime, os, requests, zipfile
from io import StringIO

def read_json(json_path):
    import json
    with open(json_path, "r") as json_data:
        data = json.load(json_data)
        json_data.close()
    return data

def download_results(url):
    r = requests.get(url, allow_redirects=True)
    # Todo: Tratar erro para python 3
    #zip_file = zipfile.ZipFile(StringIO.StringIO(r.content))
    return r

def extract_zip_file(zip_file, path):
    zip_file.extractall(path)

def put_date_in_path_string(path):
    return path + datetime.date.today().strftime("%Y-%m-%d") + "/"

def dataframe_to_csv(path, df):
    if "swamp" in path:
        file_status = "nao_tratado"
    elif "lake" in path:
        file_status = "tratado"

    print("File Status: " + file_status)

    if not os.path.exists(path):
        os.makedirs(path)
    df.to_csv(path + "/" + file_status + ".csv",sep=";", encoding="utf-8", header=1)

def get_actual_date():
    return datetime.date.today().strftime("%Y-%m-%d")

def reform_dataframe(df_megasena):
    df_formatado = df_megasena
    i = 0
    size = len(df_formatado)
    while i < size:
        if isinstance(df_formatado.iloc[i]['Concurso'], unicode) == True or \
                isinstance(df_formatado.iloc[i]['Concurso'], float) == True or \
                    not is_number(df_formatado.iloc[i]['Concurso']):
            df_formatado = concat_values(df_formatado, i)
            df_formatado = df_formatado.drop([i])
            df_formatado = df_formatado.reset_index()
            del df_formatado['index']
            i -= 1
            size -= 1
        i+=1

    df_formatado = df_formatado.set_index('Concurso')
    df_formatado['Cidade'] = df_formatado.Cidade.str.replace(r'(^.*nan.*$)', '')
    df_formatado['Cidade'] = df_formatado.Cidade.str.replace(r'(\&nbsp)', '')
    df_formatado['UF'] = df_formatado.UF.str.replace(r'(^.*nan.*$)', '')
    df_formatado['UF'] = df_formatado.UF.str.replace(r'(\&nbsp)', '')

    return df_formatado

def concat_values(df_formatado, i): 

    df_formatado.at[i-1, 'Cidade'] = unicode(df_formatado.iloc[i-1]['Cidade']) + unicode(", ") + unicode(df_formatado.iloc[i]['Concurso'])
    df_formatado.at[i-1, 'UF'] = unicode(df_formatado.iloc[i-1]['UF']) + ", " + unicode(df_formatado.iloc[i]['Data Sorteio'])

    return df_formatado

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_game_type_values(game_argument):
    
    variables = {}

    if game_argument == 'megasena':
        variables = {
            'game_type_name':game_argument,
            'game_type_zip_file_name':'D_megase.zip',
            'game_type_extracted_file_name':'D_MEGA.HTM'
        }
        return variables
    elif game_argument == 'quina':
        variables = {
            'game_type_name':game_argument,
            'game_type_zip_file_name':'D_quina.zip',
            'game_type_extracted_file_name':'D_QUINA.HTM'
        }
        return variables
    elif game_argument == 'lotofacil':
        variables = {
            'game_type_name':game_argument,
            'game_type_zip_file_name':'D_lotfac.zip',
            'game_type_extracted_file_name':'D_LOTFAC.HTM'
        }
        return variables
    elif game_argument == 'lotomania':
        variables = {
            'game_type_name':game_argument,
            'game_type_zip_file_name':'D_lotoma.zip',
            'game_type_extracted_file_name':'D_LOTMAN.HTM'
        }
        return variables
    elif game_argument == 'timemania':
        variables = {
            'game_type_name':game_argument,
            'game_type_zip_file_name':'D_timema.zip',
            'game_type_extracted_file_name':'D_TIMEMA.HTM'
        }
        return variables
    elif game_argument == 'duplasena':
        variables = {
            'game_type_name':game_argument,
            'game_type_zip_file_name':'d_dplsen.zip',
            'game_type_extracted_file_name':'D_DPLSEN.HTM'
        }
        return variables
    elif game_argument == 'federal':
        variables = {
            'game_type_name':game_argument,
            'game_type_zip_file_name':'D_federa.zip',
            'game_type_extracted_file_name':'D_LOTFED.HTM'
        }
        return variables
    elif game_argument == 'loteca':
        variables = {
            'game_type_name':game_argument,
            'game_type_zip_file_name':'D_loteca.zip',
            'game_type_extracted_file_name':'D_LOTECA.HTM'
        }
        return variables
    elif game_argument == 'lotogol':
        variables = {
            'game_type_name':game_argument,
            'game_type_zip_file_name':'D_lotogo.zip',
            'game_type_extracted_file_name':'D_LOTOGO.HTM'
        }
        return variables

    else:
        raise NameError("Invalid Parameter: " + str(game_argument))