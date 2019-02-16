# # -*- coding: utf-8 -*-

import os

def main(args=None):
    type_of_process = args[2]
    if type_of_process == 'ingest':
        import modules.ingestion as ingest
        ingest.run(args)
    elif type_of_process == 'process':
        print("Process not implemented Yet")
        pass
    return 0