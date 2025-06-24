from fastapi import FastAPI
from weatherapi import temp
import time

app = FastAPI()

# Cache com expiração (5 minutos)
last_update = 0
cache_duration = 300  # 5 minutos em segundos
cached_temp = None


"""
|------------------------------------------------------------------------------------------------------------------------------------------------------------|
|I made three tests for performance in python + fastapi and weather api, check the results and my tests below                                                |
|                                                                                                                                                            |
|First test: I created a variable (temperature) outside the route function and added only the variable (temperature) in the return (200 stats).              |
|Result {First request was 10ms, other tests 2-3ms}                                                                                                          |
|                                                                                                                                                            |
|Second test: I creted a variable (temperature) inside route function and added only the variable (temperature) in the return (200 stats).                   |
|Result {All tests returned variations from 862 to 873ms}                                                                                                    |
|                                                                                                                                                            |
|Third test: I didn't create any variables, I just added a (temporary) function in return (200 stats).                                                       |
|Result {All tests returned variations from 860 to 872ms}                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|
"""

#First test 10ms, other tests 2-3ms
def teste1(app): 
    temperature = temp()
    @app.get('/temp1')
    def get_temperature():
        try:
            return {"message": f"The temperature in my city is: {temperature} test 1",
                    "status": f"{200} OK"}
        except Exception(400):
            return{"message": "Bad Request",
                "status": 400}


#All tests returned variations from 862 to 873ms 
def teste2(app):
    @app.get('/temp2')
    def get_temperature():
        temperature = temp()
        try:
            return {"message": f"The temperature in my city is: {temperature} test 2",
                    "status": f"{200} OK"}
        except Exception(400):
            return{"message": "Bad Request",
                "status": 400}


#All tests returned variations from 860 to 872ms 
def teste3(app):
    @app.get('/temp3')
    def get_temperature():
        try:
            return {"message": f"The temperature in my city is: {temp()} test 3",
                    "status": f"{200} OK"}
        except Exception(400):
            return{"message": "Bad Request",
                "status": 400}


def teste4(app):    
    @app.get('/temp4')
    def get_temperature():
        global last_update, cached_temp

        now = time.time()
        if now - last_update > cache_duration:
            cached_temp = temp()  # Atualiza o cache
            last_update = now

        try:
            return {"message": f"The temperature in my city is: {cached_temp} test 4",
                    "status": f"{200} OK"}
        except Exception(400):
            return{"message": "Bad Request",
                "status": 400}

teste1(app)
teste2(app)
teste3(app)
teste4(app)