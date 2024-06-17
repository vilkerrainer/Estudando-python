import random
import string
import os


def verifica(numero):
        if numero.isnumeric():
            return True
        else:
            print("Digite um número")
            return False

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def gerar_senha(tamanho):
    digitos = string.ascii_letters + string.digits + string.punctuation
    
    senha = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    senha += random.choices(digitos, k=tamanho - 4)
    
    random.shuffle(senha)
    
    return ''.join(senha)

while True:
    criar_senha = input("Você deseja cirar uma senha de quantos digitos?: ")

    tamanho = criar_senha

    if verifica(tamanho):
        tamanho = int(tamanho)
        senha = gerar_senha(tamanho)

        print(f'Sua nova senha é: {senha}')
    else:
        continue    
    repetir = input("Deseja criar mais alguma senha? Y/N: ")
    
    if repetir.lower() == "y":
        limpar_terminal()
        print("Então vamos lá")
    elif repetir.lower() == "n":
        break
    else:
        print("Digite y ou n")
    