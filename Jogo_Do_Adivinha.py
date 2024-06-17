import random
from os import system

ns = random.randint(1, 10)
print(ns)

def verifica(numero):
        if numero.isnumeric():
            return True
        else:
            print("Digite um número")
            return False

while True:  
        
    chute = input("Chute um número ")
        
    if verifica(chute):
        chute = int(chute)        
        if chute == ns:
            print("Parabéns você acertou")
            break
        else:
            print("Você errou tente novamente")
    else:
        continue