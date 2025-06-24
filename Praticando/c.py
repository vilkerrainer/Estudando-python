import json

dados = 'Praticando/data.json'

idade = []


with open(dados, 'r', encoding='utf-8') as f:
    entrada = json.load(f)

for pessoa in entrada:
    idade.append(pessoa['idade'])

print(idade)
print(len(idade))