from subprocess import call

class Mcserver():
    
    def __init__(self, mcserver):
        self.mcserver = mcserver
        
    def run(self, mcserver_command, minecraft_command):
        command = self.mcserver + mcserver_command + minecraft_command
        
        call(command, shell=True)
        
    def execute(self, mine):
        print(mine)
        
    def list(self):
        mcserver_command = " sd "
        minecraft_command = " '/list'"
        #command = self.mcserver + mcserver_command + minecraft_command
        
        self.run(mcserver_command, minecraft_command)

    def whitelist(self, action, player):
        mcserver_command = " sd "
        minecraft_command = " '/whitelist "
        if action == "add":
            minecraft_command += "add " + player
        elif action == "remove":
            minecraft_command += "remove " + player
        elif action == "list":
            minecraft_command += "list"
        minecraft_command += "'"
        #command = self.mcserver + mcserver_command + minecraft_command
        
        self.run(mcserver_command, minecraft_command)
        
    def time(self, action, time):
        mcserver_command = " sd "
        minecraft_command = " '/time " + action + " " + time + "'"
        #command = self.mcserver 
        
        self.run(mcserver_command, minecraft_command)
        
    def weather(self, weather):
        mcserver_command = " sd "
        minecraft_command = " '/weather " + weather + "'"
        
        self.run(mcserver_command, minecraft_command)
            