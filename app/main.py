from fastapi import FastAPI
import platform
import os

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.get("/status")
def status():
    return {
        "container_id": os.getenv("HOSTNAME"),
        "python_version": platform.python_version(),
        "system": platform.system(),
        "platform": platform.platform()
    }

