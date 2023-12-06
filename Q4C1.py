#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math

"""
def tracao(theta, beta):
    o = (theta * math.pi) / 180  # Converter o ângulo para radianos
    b = (beta * math.pi) / 180
    T = (
        (25 * math.sqrt(745) * math.sqrt(29 + (24 * math.cos(o)) - (12 * math.sin(o))))
        / (3 * (math.cos(o)) + (2 * math.sin(o)))
    ) * math.sin(
        theta + beta
    )  # Equação geral da questão
    return T
"""

# Variáveis constantes
beta = 8.427
t = 0

T = []

# Lista para armazenar os valores de theta
# theta = np.arange(0, 120, 10)
theta = []


# Lista para armazenar os valores de peso correspondentes a theta
# T = [tracao(t, b) for t in theta]

for i in range(0, 120, 10):
    o = (i * math.pi) / 180  # Converter o ângulo para radianos
    theta.append(i)

    b = (beta * math.pi) / 180

    tracao = (
        (25 * math.sqrt(745) * math.sqrt(29 + (24 * math.cos(o)) - (12 * math.sin(o))))
        / (3 * (math.cos(o) + (2 * math.sin(o))))
    ) * math.sin(
        o + b
    )  # Equação geral da questão

    T.append(tracao)

print(f"O valor de T é {T}")
print(f"O valor MAX de T é {max(T)}")
print(f"O valor de theta é {theta}")

# """
# Função para obter os pontos de interseção
y_points = np.linspace(min(T), max(T), 100)
x_points = [theta for x in y_points]

# Configuração da figura do gráfico
plt.figure("Questão Q4.C3", figsize=(14, 5), dpi=100)

# Gráfico da curva W x theta
plt.plot(theta, T, color="blue", label="Curva W x theta")

# # Gráfico dos pontos de interseção
# for x, y in zip(theta, T):
#     plt.plot([x, x], [0, y], "k--", lw=0.5)
#     plt.plot([0, x], [y, y], "k--", lw=0.5)
# plt.plot(theta, T, color="blue")

# Configurações do gráfico
plt.ylabel("Peso W (N)")
plt.xlabel("Ângulo theta (º)")
plt.title(f"Gráfico - Questão 4.C3")
plt.legend()  # Mostra a legenda

plt.xticks(np.arange(0, max(theta), 10))
# plt.yticks(np.arange(min(T), max(T), 50))
plt.yticks(T)

plt.grid(True)
plt.show()
# """
