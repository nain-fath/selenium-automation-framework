import json
import os


class ConfigReader:

    @staticmethod
    def get_config():

        current_dir = os.path.dirname(os.path.abspath(__file__))

        project_root = os.path.dirname(current_dir)

        config_path = os.path.join(project_root, "config", "config.json")

        with open(config_path, "r") as file:
            return json.load(file)