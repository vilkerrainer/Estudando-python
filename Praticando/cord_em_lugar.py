from geopy.geocoders import Nominatim

# Inicializa o geocoder (é uma boa prática definir um user_agent)
geolocator = Nominatim(user_agent="minha-app-de-geolocalizacao")

latitude = -17.8575
longitude = -41.5053
coordenadas = f"{latitude}, {longitude}"

try:
    # Faz a chamada de geocodificação reversa
    localizacao = geolocator.reverse(coordenadas)

    # O objeto 'localizacao' tem várias informações
    print(f"Endereço Completo: {localizacao.address}")

    # Você também pode acessar os componentes do endereço
    endereco_dict = localizacao.raw['address']
    cidade = endereco_dict.get('city', '') or endereco_dict.get('town', '') or endereco_dict.get('village', '')
    estado = endereco_dict.get('state', '')
    pais = endereco_dict.get('country', '')

    print(f"Cidade: {cidade}")
    print(f"Estado: {estado}")
    print(f"País: {pais}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")