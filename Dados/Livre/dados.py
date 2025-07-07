import time
import openmeteo_requests
from openmeteo_sdk.Variable import Variable
import datetime
import os
from geopy.geocoders import Nominatim

# Configurações
CACHE_DURATION = 60  # 1 minuto em segundos
os.makedirs("Dados", exist_ok=True)  # Garante que a pasta existe


# Inicializa o geocoder (é uma boa prática definir um user_agent)
geolocator = Nominatim(user_agent="minha-app-de-geolocalizacao")

latitude = -17.8575
longitude = -41.5053
coordenadas = f"{latitude}, {longitude}"

try:
    # Faz a chamada de geocodificação reversa
    localizacao = geolocator.reverse(coordenadas)

    # Você também pode acessar os componentes do endereço
    endereco_dict = localizacao.raw['address']
    cidade = endereco_dict.get('city', '') or endereco_dict.get('town', '') or endereco_dict.get('village', '')
    estado = endereco_dict.get('state', '')
    pais = endereco_dict.get('country', '')    

except Exception as e:
    print(f"Ocorreu um erro: {e}")

def temp():
    om = openmeteo_requests.Client()

    latitude = -17.8575
    longitude = -41.5053

    params = {
        "latitude": {latitude},
        "longitude": {longitude},
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
    print(f"Cidade: {cidade}")
    print(f"Estado: {estado}")
    print(f"País: {pais}")
    with open("Dados/temp.txt", "a") as f:
        f.write(f"Temperatura {temperatura}°C, Data e Hora {data_hora.strftime('%d/%m/%Y, %H:%M:%S')}\n")




tarefa ()

# # Loop principal sincronizado com o relógio
# while True:
#     now = datetime.datetime.now()
#     next_minute = (now + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
#     delay = (next_minute - now).total_seconds()
    
#     time.sleep(delay)  # Espera até o próximo minuto redondo
#     tarefa()