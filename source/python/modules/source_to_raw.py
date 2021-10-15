import logging

class SourceToRaw:

    def __init__(self):
        pass

    def get_data_from_web_page(self, url, type="content"):
        from python.packages.custom import download_results

        response = download_results(f"{url}")
        if type == "content":
            return response.content
        return response.text

    def save_raw_data(self, dir_path, file_name, data):
        import os

        try:
            os.makedirs(dir_path, exist_ok=True)
        except:
            print(f"Path ja existe, sanvando dentro do diretorio: {dir_path}")
            pass

        with open(f"{dir_path}{file_name}", "w", encoding="utf-8") as file:
            file.write(data)
