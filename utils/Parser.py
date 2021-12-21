new = "the-different-world\\nagain"

old = "world"

ln = "level-name="

with open(r"server.properties", "r") as file:
    data = file.read()
    data = data.replace(ln+old, ln+new)
    
with open(r"server.properties", "w") as file:
    file.write(data)


'''

class Parser():
    
    def parse_properties(self, file_path):
        
    def load_file(self, file):
        opened_file = open(file)
'''        