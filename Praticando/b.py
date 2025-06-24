# import random
import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x)
y5 = x**2

# Criar figura
fig = plt.figure(figsize=(12, 6))

# Altura e largura padrão dos gráficos
w, h = 0.25, 0.35  # largura e altura dos gráficos

# Linha de cima (g1, g2, g3)
ax1 = fig.add_axes([0.05, 0.55, w, h])
ax2 = fig.add_axes([0.375, 0.55, w, h])
ax3 = fig.add_axes([0.70, 0.55, w, h])

# Linha de baixo (g4 entre g1 e g2, g5 entre g2 e g3)
ax4 = fig.add_axes([0.21, 0.08, w, h])
ax5 = fig.add_axes([0.54, 0.08, w, h])

# Plotar gráficos
ax1.plot(x, y1)
ax1.set_title("g1")

ax2.plot(x, y2)
ax2.set_title("g2")

ax3.plot(x, y3)
ax3.set_title("g3")
ax3.set_ylim(-10, 10)

ax4.plot(x, y4)
ax4.set_title("g4 (entre g1 e g2)")

ax5.plot(x, y5)
ax5.set_title("g5 (entre g2 e g3)")

plt.show()


# x = []
# Xi = 0
# loop = True

# while loop:
#     Xi = Xi + 0.01
#     # print(Xi)
#     x.append(Xi)
#     result = '%.0f' %(Xi)
#     fim = '%.0f' %(10)
#     print(result)

#     if result == fim:
#         loop = False

# print(x)

# for i in range(10):
#     valor = random.uniform(1.1, 3.6)
#     if (valor < resultado[i]):
#         resultado.append(valor)
#     print('%.5f' %(valor))
#     print(resultado)