import json

def load_file(config_file):
    opened_file = open(config_file)

    data = json.load(opened_file)

    return data


