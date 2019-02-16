import requests, re, sys, traceback

def format_error_as_string(exception):
    formated =  """    
    ###############################################################################\n
        ERRO AO PROCESSAR!!! \n
        Detalhes: \n
        {0}\n
        {1}\n
    ###############################################################################"""\
    .format(traceback.format_exc(), str(exception))
    return formated

try:
    html_text = requests.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena').text
    resultados = re.search(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.\b.([-a-zA-Z0-9@:%_\+.~#?&//=]*)\.zip', html_content)

    print resultados

except Exception as e:
    print format_error_as_string(e)


