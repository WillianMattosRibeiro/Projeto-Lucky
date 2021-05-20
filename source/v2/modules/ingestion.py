from ..packages.custom import *

class Processamento(object):
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

            print_console_presentation('Demonstracao gitflow')
        except Exception as e:
            print get_error_formated_as_string(e)