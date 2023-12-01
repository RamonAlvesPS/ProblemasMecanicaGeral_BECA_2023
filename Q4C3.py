""" DESCRIÇÃO
	Instituição:
        INSTITUTO FEDERAL DA PARAÍBA - Campus Cajazeiras
    Autor: 
        Ramon Alves
    Data de inicio: 
        30/11/2023
    Professor: 
        Anrafel 
    Disciplina:
		Mecânica Geral
    Objetivo: 
        Implementar um script para solucionar as vigas da questão 5C.1 do livro "Mecânica para Engenharia" do Beer.
    Arquivo:
		
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Essas duas linhas são comentários especiais usados para configurar o ambiente de execução do código.

import matplotlib.pyplot as plt
plt.rcParams['figure.facecolor'] = 'white'

import numpy as np

import math

from colorama import Fore, Style, init
# Inicializar colorama
init(autoreset=True)

W = 0 # Peso 
peso = [] 
k = 1000 # Constante da Mola AB, em N
a = 500/1000 # Distancia entre os 2 apoios, em m
R = 250/1000 # Raio, em m
o = 0 # Theta, angulo do ponto B até o Apoio A, em º
# o = 16.5845 # Theta
# o = (16.5845*math.pi)/180 # Theta
theta = []

for i in range(0, 100, 10):
    o = (i*math.pi)/180 # Theta
    theta.append(i)

    W = k*(math.sqrt((R**2)+(a**2)-(2*a*R*(math.cos(o))))-a+R) # Equação geral da questão
    peso.append(W)

# print(f'O valor de W é {W}')
# print(theta)
# print(peso)

plt.figure('Questão Q4.C3', figsize=(15,5), dpi=100)

for x, y in zip(peso, theta):
    plt.plot([x,x], [0,y], 'k--', lw=0.5)
    plt.plot([0,x], [y,y], 'k--', lw=0.5)
plt.plot(peso, theta, color='red')

# Settings
# plt.legend()
plt.xlabel('Peso W (N)')
plt.ylabel('Angulo theta (º)')
plt.title(f'Grafico  da Questão')

# plt.xticks(np.arange(0, max(peso)+10, 30))
plt.yticks(np.arange(0, max(theta), 10))
plt.yticks(theta)
plt.xticks(peso)

plt.show()
