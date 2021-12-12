import json

class Config():
    MCMANAGER_FILE = "./config/mcmanager.json"
    MCSERVER_FILE = "./config/mcserver.json"
    MINECRAFT_FILE = "./config/minecraft.json"
    
    mcmanager_config = {}
    mcserver_config = {}
    minecraft_config = {}
    
    def load_mcmanager(self):
        self.load_json(self.MCMANAGER_FILE)
        
    def load_mcserver(self):
        self.load_json(self.MCSERVER_FILE)
        
    def load_minecraft(self):
        self.load_json(self.MINECRAFT_FILE)
        
    def load_json(self, file):
        opened_file = open(file)
        loaded_data = json.load(opened_file)
        return loaded_data
        
        

def load_config():
    opened_file = open("./config/mcserver.json")

    data = json.load(opened_file)
    
    print(data["commands"]["lgsm"][""])

    return data


