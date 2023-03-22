from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from rcon.source import Client

import subprocess
#from jproperties import Properties 

#region Flask Initialization

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

#endregion

@app.route("/")
def main():
    page = "main"

    response = make_response(
        render_template(
            page + ".html",
            page=page
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

@app.route("/syncworld",methods = ['POST'])
def sync_world():
    # rsync -rvh --info=progress2 --info=name0 mcserver@10.0.0.101:/opt/mcserver/serverfiles/world ./
    with Client('127.0.0.1', 25575, passwd='adminR0HbEq6t') as client:
            response = client.run('/op', 'RedwardFlip')

    print(response)
    return response

#region Run Flask

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
    )
    
#endregion
