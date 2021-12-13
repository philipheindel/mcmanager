import json

class Config():
    
    def load_mcmanager(self, mcmanager_file="./config/mcmanager.json"):
        return self.load_json(mcmanager_file)
        
    def load_mcserver(self, mcserver_file="./config/mcserver.json"):
        return self.load_json(mcserver_file)
        
    def load_minecraft(self, minecraft_file="./config/minecraft.json"):
        return self.load_json(minecraft_file)
        
    def load_json(self, file):
        opened_file = open(file)
        loaded_data = json.load(opened_file)
        return loaded_data
        
