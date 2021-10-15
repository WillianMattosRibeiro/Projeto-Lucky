import pandas as pd


class RawRoStaging:

    def __init__(self):
        pass

    def load_html(self, html_path):
        tables = pd.read_html(html_path)
        # TODO: Entender por que com parametro quina encontra 1879 tables no HTMl
        print('Tables found:', len(tables))
        raise

    def save_staging_data(self, pandas_df, staging_path, file_name):
        import os
        dataFrame = pd.DataFrame(data=pandas_df, index=None)

        try:
            os.makedirs(staging_path, exist_ok=True)
        except:
            print(f"Path ja existe, sanvando dentro do diretorio: {staging_path}")
            pass

        dataFrame.to_csv(f"{staging_path}{file_name}", encoding="utf-16")
