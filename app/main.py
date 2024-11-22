"""
Simple fastapi to test tailscale operator and funnel
"""

import platform
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    """
    Return a simple hello message 
    """
    return {"message": "Hello, World!"}

@app.get("/status")
def status():
    """
    Return container and host information
    """
    return {
        "container_id": os.getenv("HOSTNAME"),
        "python_version": platform.python_version(),
        "system": platform.system(),
        "platform": platform.platform()
    }
