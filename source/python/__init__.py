import traceback

import pandas

from python.modules.configuration import Configuration
from python.modules.source_to_raw import SourceToRaw
from python.modules.raw_to_staging import RawRoStaging

import logging

def main(args=None):

    log = logging.getLogger()
    conf = Configuration()
    str = SourceToRaw()
    rts = RawRoStaging()

    games_list = conf.get_game_list()

    try:
        game = args[1]
    except Exception as e:
        log.error("Blank Argument!")
        raise e

    if game not in games_list:
        log.error("ERROR: Invalid Argument passed, Valid arguments are: {}".format(games_list))
        raise traceback.TracebackException

    # capturar as configuracoes do jogo passado como parametro
    config = conf.get_game_config(game)

    # capturar resultados da pagina html do jogo
    data_content = str.get_data_from_web_page(f"{config['base_url']}{config['game_conf']['url']}", "text")
    #print(f"url: {config['base_url']}{config['game_conf']['url']}")

    # salvar o html na camada raw
    from datetime import datetime
    local_dir = conf.get_local_dir()
    today = datetime.now().strftime("%Y-%m-%d")
    raw_path = f"{local_dir}\\{config['base_raw_path']}\\{today}\\{game}\\"
    file_raw_name = f"resultado_{game}.txt"
    str.save_raw_data(raw_path, file_raw_name, data_content)

    # ler o html da raw, transformar em csv, salvar na camada swamp
    html_dataframe = rts.load_html(f"{raw_path}{file_raw_name}")
    staging_path = f"{local_dir}\\{config['base_staging_path']}\\{today}\\{game}\\"
    file_staging_name = f"resultado_{game}.csv"

    rts.save_staging_data(html_dataframe, staging_path, file_staging_name)

    # ler o csv da camada swamp, tratar datas e valores, tipar colunas e salvar na camada lake como csv
