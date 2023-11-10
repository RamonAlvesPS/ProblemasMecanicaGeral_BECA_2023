# Questão 5.C1 do livro Mecânica Beer

import matplotlib.pyplot as plt
import numpy as np

def calcula_esforco_cortante(dados):
    L = dados[0] # Comprimento total da viga
    n = dados[1] # Número de nós na viga
    c = dados[2] # Módulo de elasticidade do material da viga
    W = dados[3] # Peso total aplicado à viga

    # Montagem da matriz de coeficientes
    matriz_coeficientes = np.zeros((n, n))
    matriz_coeficientes[0][0] = -c / 2
    matriz_coeficientes[0][1] = c / 2
    matriz_coeficientes[n - 1][n - 2] = -c / 2
    matriz_coeficientes[n - 1][n - 1] = c / 2

    for i in range(1, n - 1):
        matriz_coeficientes[i][i - 1] = -c / 2
        matriz_coeficientes[i][i + 1] = -c / 2
        matriz_coeficientes[i][i] = c

    # Montagem do vetor de incógnitas
    vetor_incognitas = np.zeros(n)
    vetor_incognitas[0] = -c / 2
    vetor_incognitas[n - 1] = -c / 2

    # Montagem do vetor de pesos
    vetor_pesos = np.zeros(n)
    vetor_pesos[0] = -c / 2
    vetor_pesos[n - 1] = -c / 2

    # Aplicação do método de Newton-Raphson
    delta_y = np.linalg.solve(matriz_coeficientes, vetor_incognitas)
    delta_x = np.linspace(0, L, n)

    # Calcula do esforço cortante e momento fletor
    vetor_esforco_cortante = W * np.linspace(0, L, n) - delta_y
    vetor_momento_fletor = (
        -delta_y * np.linspace(0, L, n) + (W / 2) * np.linspace(0, L, n) ** 2
    )

    return delta_x, vetor_esforco_cortante, vetor_momento_fletor


# Exemplo de uso
dados = [5, 5, 210000, 1000]
delta_x, vetor_esforco_cortante, vetor_momento_fletor = calcula_esforco_cortante(dados)

# Visualização do esforço cortante
plt.plot(delta_x, vetor_esforco_cortante)
plt.title("Esforço Cortante")
plt.xlabel("Posição ao longo da viga (m)")
plt.ylabel("Esforço Cortante (N)")
plt.show()

# Visualização do momento fletor
plt.plot(delta_x, vetor_momento_fletor)
plt.title("Momento Fletor")
plt.xlabel("Posição ao longo da viga (m)")
plt.ylabel("Momento Fletor (N*m)")
plt.show()
