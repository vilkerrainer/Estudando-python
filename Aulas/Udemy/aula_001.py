#Interpolar

"""
|========================================|
|s - string                              |
|d e i - int                             |
|f - float                               |
|x e X - Hexadecimal (ABCDEF0123456789)  |
|========================================|
"""

nome = 'Vilker'
preco = 124.54784

juntar = '%s, o preco é de R$%.2f' %(nome, preco)

print(juntar)
print('O hexadecimal de %d é %04x' % (15, 15)) 