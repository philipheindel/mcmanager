from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rcon.source import Client

import subprocess

api = FastAPI()

origins = ["*"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/")
def root():
    return { "Hellow": "World"}

@api.post("/CopyWorld")
def copy_world():
    # rsync -rvh --info=progress2 --info=name0 mcserver@10.0.0.101:/opt/mcserver/serverfiles/world ./
    
    subprocess.call(["rsync", "-rvh", "--info=progress2", "--info=name0", "mcserver@10.0.0.101:/opt/mcserver/serverfiles/world", "/opt/mcserver/"])

    #subprocess.call(["whoami"])


    
    #rint(response)
    return ""


@api.post("/StartServer")
def start_server():
    
    subprocess.call(["/opt/mcserver/mcserver", "start"])

    return ""


@api.post("/StopServer")
def stop_server():
    
    subprocess.call(["/opt/mcserver/mcserver", "stop"])

    print("Server stopped?")
    return ""