import time
import openmeteo_requests
from openmeteo_sdk.Variable import Variable
import datetime
import os

# Configurações
CACHE_DURATION = 60  # 1 minuto em segundos
os.makedirs("Dados", exist_ok=True)  # Garante que a pasta existe

def temp():
    om = openmeteo_requests.Client()
    params = {
        "latitude": -17.8575,
        "longitude": -41.5053,
        "hourly": ["temperature_2m"],
        "current": ["temperature_2m"]
    }
    responses = om.weather_api("https://api.open-meteo.com/v1/forecast", params=params)
    response = responses[0]
    current = response.Current()
    current_variables = list(map(lambda i: current.Variables(i), range(0, current.VariablesLength())))
    current_temperature_2m = next(filter(lambda x: x.Variable() == Variable.temperature and x.Altitude() == 2, current_variables))
    return f"{current_temperature_2m.Value():.0f}"

def tarefa():
    temperatura = temp()
    data_hora = datetime.datetime.now()
    
    print(f"Temperatura {temperatura}°C, Data e Hora {data_hora.strftime('%d/%m/%Y, %H:%M:%S')}")
    with open("Dados/temp.txt", "a") as f:
        f.write(f"Temperatura {temperatura}°C, Data e Hora {data_hora.strftime('%d/%m/%Y, %H:%M:%S')}\n")

# Loop principal sincronizado com o relógio
while True:
    now = datetime.datetime.now()
    next_minute = (now + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
    delay = (next_minute - now).total_seconds()
    
    time.sleep(delay)  # Espera até o próximo minuto redondo
    tarefa()