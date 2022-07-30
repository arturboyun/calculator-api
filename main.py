# http://127.0.0.1:8000/add?a=10&b=10
#
# http://127.0.0.1:8000/substract?a=10&b=10
#
# http://127.0.0.1:8000/divide?a=10&b=10
#
# http://127.0.0.1:8000/multiply?a=10&b=10
#
# Params: a, b
#
# {"result": result}
#
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/add")
async def add(a: Union[int, float], b: Union[int, float]):
    return {"result": a + b}


@app.get("/subtract")
async def add(a: Union[int, float], b: Union[int, float]):
    return {"result": a - b}


@app.get("/divide")
async def add(a: Union[int, float], b: Union[int, float]):
    # try:
    if b == 0:
        return {"result": "You can't divide by zero."}
    return {"result": a / b}
    # except ZeroDivisionError:
    #     return {"result": "You can't divide by zero."}


@app.get("/multiply")
async def add(a: Union[int, float], b: Union[int, float]):
    return {"result": a * b}
