from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from utils.Mcserver import Mcserver
from utils.Config import Config
#from jproperties import Properties

#region Load Configs

config_loader = Config()
mcmanager_config = config_loader.load_mcmanager()
mcserver_config = config_loader.load_mcserver()
minecraft_config = config_loader.load_minecraft()

#endregion

#region File Path Assembly

root_directory = mcserver_config["root_directory"]
mcserver_script = Mcserver(root_directory + mcserver_config["mcserver"])
serverfiles_directory = root_directory + mcserver_config["serverfiles"]
server_properties_file = serverfiles_directory + mcserver_config["server_properties"]
whitelist_file = serverfiles_directory + mcserver_config["whitelist"]
ops_file = serverfiles_directory + mcserver_config["ops"]
banned_ips_file = serverfiles_directory + mcserver_config["banned_ips"]
banned_players_file = serverfiles_directory + mcserver_config["banned_players"]
#print(server_properties_file)
#p = Properties()
#with open(server_properties_file, "rb") as f:
#    p.load(f)

#endregion

#region Flask Initialization

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

#endregion

#region Page Endpoints

@app.route("/")
def main():
    page = "main"

    response = make_response(
        render_template(
            page + ".html",
            page=page
        )
    )
    #response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/players")
def players():
    page = "players"
    
    whitelist = config_loader.load_json(whitelist_file)
    
    response = make_response(
        render_template(
            page+".html",
            page="players",
            whitelist=whitelist
        )
    )
    return response

@app.route("/world")
def world():
    page = "world"
    
    response = make_response(
        render_template(
            page+".html",
            page=page
        )
    )
    return response

@app.route("/server")
def server():
    
    return 200

#endregion

#region API Endpoints

@app.route("/execute/<command>", methods = ["POST"])
def execute(command):
    try:
        print(command)
        mcserver_script
    except BaseException as err:
        print(err)
    return "Ran " + command, 200



@app.route("/time", methods = ["POST"])
def time():
    try:
        data = request.json
        action = data["action"]
        time = data["time"]
        mcserver_script.time(action, time)

        response = make_response(
            200
        )
    except BaseException as err:
        print("oh no! our table! it's broken!")
        
    return "set time to day", 200

@app.route("/weather", methods = ["POST"])
def weather():
    
    data = request.json
    weather = data["weather"]
    
    mcserver_script.weather(weather)
    
    return "set weather to clear", 200
    
#endregion

#region Run Flask

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
    )
    
#endregion
