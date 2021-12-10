from flask import Flask
from flask import render_template
from subprocess import call
import json

manager_folder = "/opt/mcserver/mcmanager"
mcserver_folder = "/opt/mcserver"
serverfiles_folder = mcserver_folder + "/serverfiles"

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

@app.route("/")
def home():
    touch = "/usr/bin/touch"

    call(mcserver_folder + "/mcserver sd '/list'", shell=True)

    f = open('/opt/mcserver/serverfiles/whitelist.json')
    data = json.load(f)
    whitelist = data

    # whitelist = [ "RedwardFlip", "whatmind" ]
    return render_template(
        'main.html',
        whitelist=whitelist
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')
