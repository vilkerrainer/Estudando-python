from fastapi import FastAPI
from pydantic import BaseModel
from passlib.context import CryptContext

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Pessoa(BaseModel):
    nome: str
    valor: str

@app.post("/conta/create")
async def create_poeple(pessoa: Pessoa):
    senha = pessoa.senha
    senha_hash = pwd_context.hash(senha)
    return {f"{pessoa} e a senha seria {senha_hash}"}