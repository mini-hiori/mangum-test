# ref: https://github.com/TatchNicolas/sls-mangum-fastapi/blob/master/exam_results/main.py
from typing import List

from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel

app = FastAPI()


class HelloParam(BaseModel):
    name: str


@app.get("/hello")
def get_hello(name: str = None):
    """
    getでおへんじする
    """
    if name:
        message = f"[GET]hello, {name}!"
    else:
        message = f"[GET]hello, visitor!"

    return {"message": message}


@app.post("/hello_post")
def post_hello(param: HelloParam):
    """
    postでおへんじする
    """
    if not param.name:
        raise HTTPException(status_code=400, detail="おなまえがないよ")
    else:
        message = f"[GET]hello, {param.name}!"

    return {"message": message}


handler = Mangum(app)
