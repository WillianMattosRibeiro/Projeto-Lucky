from python.packages.custom import read_json
import os

LOCAL_DIR = ""


class Configuration:

    def __init__(self):
        self.LOCAL_DIR = self.get_local_dir()

    def get_local_dir(self):
        return os.path.abspath(os.curdir)

    def get_game_list(self):
        json_path = "{}\\source\\json_config\\games_list.json".format(self.LOCAL_DIR)
        data = read_json(json_path)
        return [key for key in data["games"]]

    def get_game_config(self, game):
        json_path = "{}\\source\\json_config\\games_list.json".format(self.LOCAL_DIR)
        data = read_json(json_path)
        return {
            "base_url": data["base_url"],
            "base_raw_path": data["base_raw_path"],
            "base_staging_path": data["base_staging_path"],
            "base_lake_path": data["base_lake_path"],
            "game_conf": data["games"][game]
        }
