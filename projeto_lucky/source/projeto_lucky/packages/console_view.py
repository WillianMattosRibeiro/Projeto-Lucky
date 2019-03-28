import os, requests, re, sys, traceback

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