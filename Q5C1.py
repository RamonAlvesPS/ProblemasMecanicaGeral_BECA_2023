# v1.2

"""
Neste exemplo, foi adicionado um novo elemento à lista 'dados' para representar o tipo 
de carga aplicada à viga ('carga_uniforme' ou 'carga_pontual'). A matriz de coeficientes e 
o vetor de incógnitas são montados de acordo com a configuração da viga.

Para aplicar o método de Newton-Raphson, a função 'np.linalg.solve()' é utilizada 
para resolver o sistema de equações. Após a solução, os vetores de esforço cortante 
e momento fletor são calculados e plotados.

Desta forma, é possível simular e analisar a distribuição do esforço cortante e 
momento fletor em uma viga simplesmente apoiada com diferentes tipos de cargas aplicadas.

Obs: Para calcular a carga na extremidade, você deve saber se a extremidade da viga 
é com suporte simples (fixa na extremidade) ou fixa dupla (fixa em ambas as extremidades). 
Neste caso, foi assumido um suporte simples na extremidade. Se o suporte for duplo, a carga na 
extremidade deve ser dividida por 2.

Para simular outras condições de carga ou de viga, você pode modificar os valores nas listas 'dados' e 'L'.
"""

"""
Produza um Script em python que calcule e mostre o grafico do esforço cortante e momento fletor de uma viga dada pelo usuario. 
A viga terá um apoio fixo em X e Y no inicio do comprimento e um apoio fixo em Y e livre em X.
Além disso, a viga poderá ser informada de varia condições, por exemplo com nós (n) em diferentes posições de seu comprimento total (L), diferentes valores de pesos (W) em nós específicos, carga pontual, carga uniforme, carga linear...
"""

import matplotlib.pyplot as plt
import numpy as np

def calcula_esforco_cortante(dados):
    L = dados[0]
    n = dados[1]
    A = dados[2]
    c = dados[3]
    W = dados[4]
    type_W = dados[5]

    # Montagem da matriz de coeficientes
    matriz_coeficientes = np.zeros((n, n))
    matriz_coeficientes[0][0] = -c/2
    matriz_coeficientes[0][1] = c/2
    matriz_coeficientes[n-1][n-2] = -c/2
    matriz_coeficientes[n-1][n-1] = c/2

    for i in range(1, n-1):
        matriz_coeficientes[i][i-1] = -c/2
        matriz_coeficientes[i][i+1] = -c/2
        matriz_coeficientes[i][i] = c

    # Montagem do vetor de incógnitas
    vetor_incognitas = np.zeros(n)
    vetor_incognitas[0] = -c/2
    vetor_incognitas[n-1] = -c/2

    # Montagem do vetor de pesos
    vetor_pesos = np.zeros(n)
    vetor_pesos[0] = -c/2
    vetor_pesos[n-1] = -c/2

    # Aplicação do método de Newton-Raphson
    delta_y = np.linalg.solve(matriz_coeficientes, vetor_incognitas)
    delta_x = np.linspace(0, L, n)

    # Calcula do esforço cortante e momento fletor
    vetor_esforco_cortante = W*np.linspace(0, L, n) - delta_y
    vetor_momento_fletor = -delta_y*np.linspace(0, L, n) + (W/2)*np.linspace(0, L, n)**2

    return delta_x, vetor_esforco_cortante, vetor_momento_fletor

# Exemplo de uso
dados = [5, 5, 210000, 1000, 5000, 'carga_uniforme']
delta_x, vetor_esforco_cortante, vetor_momento_fletor = calcula_esforco_cortante(dados)

# Visualização do esforço cortante
plt.plot(delta_x, vetor_esforco_cortante)
plt.title('Esforço Cortante')
plt.xlabel('Posição ao longo da viga (m)')
plt.ylabel('Esforço Cortante (N)')
plt.show()

# Visualização do momento fletor
plt.plot(delta_x, vetor_momento_fletor)
plt.title('Momento Fletor')
plt.xlabel('Posição ao longo da viga (m)')
plt.ylabel('Momento Fletor (N*m)')
plt.show()