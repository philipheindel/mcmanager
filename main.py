from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from subprocess import call
import json
from utils.Mcserver import Mcserver
from utils.Config import Config

config = Config()
config.load_mcmanager()
config.load_mcserver()
config.load_minecraft()

mcserver = Mcserver("/home/philip/mcserver/mcserver")

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

@app.route("/")
def home():
    

    f = open('/home/philip/mcserver/serverfiles/whitelist.json')
    data = json.load(f)
    whitelist = data
    
    response = make_response(
        render_template(
            "main.html",
            whitelist=whitelist
        )
    )
    
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

@app.route("/execute/<command>", methods = ["POST"])
def execute(command):
    print(command)
    return "Ran " + command, 200

@app.route("/time", methods = ["POST"])
def time():
    try:
        data = request.json
        action = data["action"]
        time = data["time"]
        mcserver.time(action, time)

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
    
    mcserver.weather(weather)
    
    return "set weather to clear", 200
    

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
    )
