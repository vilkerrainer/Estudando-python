import string
import random
import time
import os

os.system('cls')

def teste(tamanho):
    contador = 1
    inicio = time.time()
    medida = ""
    lista = []

    def gerar_senha(tamanho):
        caracteres = string.ascii_letters + string.digits
        senha = ''.join(random.choice(caracteres) for i in range(tamanho))
        return senha

    while True:
        fim = time.time()
        senha = gerar_senha(tamanho)
        contador = contador + 1
        lista.append(f"senha numero: {contador} foi: {senha}")
        
        
        if fim - inicio < 1:
            medida = "ms"
        else:
            medida = "s"
        
        print(f"tentativa de número {contador} a senha foi {senha}")
        
        if senha == "f11":
            print(f"Você achou a o {senha} em {contador} tentativas")
            print(f"\nO Tempo gasto foi de {fim - inicio:.2f}{medida}")
            break
        else:
            continue

    return "Achou"

teste(3)
