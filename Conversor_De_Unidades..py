import os

def verifica(numero):
    try:
        float(numero)
        return True
    except ValueError:
        print("Digite um número válido.")
        return False

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def c_km(comprimento, medida):
    conversoes = {
        "km": 1,
        "hm": 10.0,
        "dam": 100.0,
        "m": 1000.0,
        "dm": 10000.0,
        "cm": 100000.0,
        "mm": 1000000.0
    }
    
    if medida in conversoes:
        return comprimento * conversoes[medida]
    else:
        print("Medida inválida")
        return None

def c_resto(comprimento, medida):
    conversoes = {
        "km": 1,
        "hm": 10.0,
        "dam": 100.0,
        "m": 1000.0,
        "dm": 10000.0,
        "cm": 100000.0,
        "mm": 1000000.0
    }
    
    if medida in conversoes:
        return comprimento / conversoes[medida]
    else:
        print("Medida inválida")
        return None

while True:  
    receber_Comprimento = input("Qual medida pretende converter? Escolha entre: km, hm, dam, m, dm, cm, mm: ")
    converter_Para = input("Para qual medida deseja converter? Escolha entre: km, hm, dam, m, dm, cm, mm: ")    
    
    tamanho = input("Qual o comprimento? ")
    if verifica(tamanho):
        tamanho = float(tamanho)        
        
        conversao_Total = c_resto(tamanho, receber_Comprimento)
        if conversao_Total is not None:
            tamanhos = c_km(conversao_Total, converter_Para)
            if tamanhos is not None:
                print(f'{tamanho} {receber_Comprimento} é igual a {tamanhos} {converter_Para}')
        
        repetir = input("Deseja calcular algo mais? Y/N: ")
        
        if repetir.lower() == "y":
            limpar_terminal()
            print("Então vamos lá")
        elif repetir.lower() == "n":
            break
        else:
            print("Digite y ou n")
    else:
        continue
