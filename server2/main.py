from typing import Union

import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    r = requests.get("http://test_server_1:5500/").json()
    r[1] = 2
    return r


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5500, log_level="info", reload=True)