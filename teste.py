import string
import random
import time

contador = 1
inicio = time.time()
medida = ""

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

while True:
    fim = time.time()
    senha = gerar_senha(4)
    contador += 1
    
    
    if fim - inicio < 1:
        medida = "ms"
    else:
        medida = "s"
    
    print(f"{contador} tentativas")
    
    if senha == "jC7t":
        print(f"Você achou a o {senha} em {contador} tentativas")
        print(f"\nO Tempo gasto foi de {fim - inicio:.2f}{medida}")
        break
    else:
        continue