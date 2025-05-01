#Média 20s
import json
from fastapi import FastAPI

app = FastAPI()

def teste(n: int) -> int:
    a, b = 0, 1
    for n in range(n):
        a, b = b, a + b
    return a

def fib(n):
    a, b = 0, 1
    for n in range(n):
        a, b = b, a + b
    return a

@app.get("/fib/{n}")
async def calculate_fib(n: int):
    result = fib(n)
    return {"result": result}

@app.get("/arquivo")
async def receber_arquivo():
    with open('data.json', 'r') as f:
        dados = json.load(f)
    return {"resultado": dados}