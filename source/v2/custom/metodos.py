# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

#Algoritmo para download de um arquivo .zip e extracao em uma pasta especificada

#Bibliotecas
import datetime, os, requests, StringIO, zipfile, unicodedata
import pandas as pd

def run(args=None):

    game_name = str(args[1])
    print_console_presentation('Resultados Jogos Caixa Economica Feredal', game_name)

    try:
        variables_dict = get_game_type_values(str(args[1]))

        raw_path = put_date_in_path_string(os.getcwd() + "/output/data/raw/" + variables_dict['game_type_name'] + "/")
        swamp_path = put_date_in_path_string(os.getcwd() + "/output/data/swamp/" + variables_dict['game_type_name'] + "/")
                    
        print_console_presentation('Baixando Arquivos...', game_name)
        zip_file = download_results('http://www1.caixa.gov.br/loterias/_arquivos/loterias/' + variables_dict['game_type_zip_file_name'])

        print_console_presentation('Extraindo dados Arquivos...', game_name)
        extract_zip_file(zip_file, raw_path)

        print_console_presentation('Carregando Dados do Raw...', game_name)
        list_megasena = pd.read_html(raw_path + "/" + variables_dict['game_type_extracted_file_name'], header=0, thousands=' ')[0]

        print_console_presentation('Formatando Dataframe...', game_name)
        df_result = reform_dataframe(list_megasena)

        print_console_presentation('Carregando Arquivos em CSV...', game_name)
        dataframe_to_csv(swamp_path, df_result)

        print_console_presentation('Ingestao Finalizada com sucesso... ', game_name)
    except Exception as e:
        print get_error_formated_as_string(e)

def download_results(url):
    r = requests.get(url, stream='true')
    zip_file = zipfile.ZipFile(StringIO.StringIO(r.content))
    return zip_file

def extract_zip_file(zip_file, path):
    zip_file.extractall(path)

def put_date_in_path_string(path):
    return path + datetime.date.today().strftime("%Y-%m-%d") + "/"

def dataframe_to_csv(path, df):
	if not os.path.exists(path):
		os.makedirs(path)
	df.to_csv(path + "/nao_tratado.csv",sep=";", encoding="utf-8", header=1)

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

def get_error_formated_as_string(exception):

    if exception.__class__ == requests.exceptions.ConnectionError:
        formated =  """
        ###############################################################################\n
            Connection Error!!! \n
            Details: \n
                {0}\n
        ###############################################################################"""\
        .format(str(exception))
    elif exception.__class__ == requests.exceptions.MissingSchema:
        formated =  """
        ###############################################################################\n
            Invalid URL!!! \n
            Details: \n
                {0}\n
        ###############################################################################"""\
        .format(str(exception))
    elif exception.__class__ == NameError:
        formated =  """
        ###############################################################################\n
            Invalid Parameter!!! \n
            Details: \n
                {0}\n
        ###############################################################################"""\
        .format(str(exception))
    else:
        import traceback
        formated =  """    
        ###############################################################################\n
            EXCECAO NAO PREVISTA!!! \n
            Detalhes: \n
                Traceback:\n
                {0}\n
                Exception:\n
                {1}\n
                Type:
                {2}\n
        ###############################################################################"""\
        .format(traceback.format_exc(), str(exception), type(exception))
    return formated

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

# GUI PRESENTATION #

def print_console_presentation(text, game_type=None):
    
    os.system('cls')
    layout = "_"
    for i in range(len(" __________________________________________________________")):
        layout += "_"
    layout += "\n"

    print ("\n" + layout)
    print("{0}").format(calculate_center(layout, 'Projeto - Lucky'))
    print("{0}").format(calculate_center(layout, 'Ingestao de Dados Loterias Caixa'))
    print("{0}").format(calculate_center(layout,game_type))

    print ("\n" + layout)
    print ("{0}").format(calculate_center(layout,text))
    print (layout)
   
def calculate_center(reference, text):
    string_size = len(text)
    space_size = (len(reference)-string_size)//2
    space_string = ""
    for i in range(space_size):
        space_string += " "
        i+=1
    return space_string + text + space_string