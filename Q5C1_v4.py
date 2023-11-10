# V 1.4

"""
Produza um Script em python que calcule e mostre o gráfico do esforço cortante e momento fletor de uma viga dada pelo usuario. 
A viga terá um apoio fixo em X e Y no inicio do comprimento e um apoio fixo em Y e livre em X.
Além disso, a viga poderá ser informada de varia condições, por exemplo com nós (n) em diferentes posições de seu comprimento total (L), diferentes valores de pesos (W) em nós específicos, e o tipo de carga (pontual, uniforme, linear...) em cada nó (inicial a final) informado.

"""

import numpy as np
import matplotlib.pyplot as plt

# Valores de entrada do usuário
E = float(input('Entre com o módulo de elasticidade da viga: '))
I = float(input('Entre com o momento de inércia da viga: '))
L = float(input('Entre com o comprimento total da viga: '))

n = int(input('Entre com o número de nós (2 a L-1): '))
nodes = [float(input(f'Entre com a posição do nó {i+1}: ')) for i in range(n)]
weights = [float(input(f'Entre com o peso do nó {i+1}: ')) for i in range(n)]

cargas = {}
for i in range(n):
    carga_tipo = input(f'Entre com o tipo de carga no nó {i+1} (P para pontual, U para uniforme, L para linear): ')
    carga_valor = float(input(f'Entre com o valor da carga no nó {i}: '))
    cargas[i] = {'tipo': carga_tipo, 'valor': carga_valor}

"""
for i in range(n+1):
    carga_tipo = input(f'Entre com o tipo de carga no nó {i+1} (P para pontual, U para uniforme, L para linear): ')
    carga_valor = float(input(f'Entre com o valor da carga no nó {i+1}: '))
    cargas[i] = {'tipo': carga_tipo, 'valor': carga_valor}
"""

# Calcula os coeficientes do polinômio de interpolação
def lagrange(x, n, nodes):
    print(f'X: ', x)
    print(f'N: ', n)
    print(f'Nodes: ', nodes)

    li = [1]*n
    print(f'Li: ', li)

    for i in range(n):
        li[i] *= x
        for j in range(i):
            li[i] *= (x - nodes[j])
        li[i] = 1 / li[i]
    return li

# Calcula o esforço cortante e o momento fletor em cada posição do elemento
def calc_esforco_momento(E, I, n, nodes, weights, cargas):
    #li = lagrange(0, n, nodes)
    li = lagrange(1, n, nodes)
    for i in range(n+1):
        for j in range(n):
            li[j] *= cargas[j]['valor']
        for j in range(n):
            li[j] *= (0 - nodes[j])
        W = sum(li[j]*weights[j] for j in range(n))
        M = -E * I * sum(li[j] for j in range(n))
        print(f'Posição: {i/n*L:.2f}, Esforço Cortante: {W:.2f}, Momento Fletor: {M:.2f}')

# Imprime o gráfico do esforço cortante e do momento fletor
def plot_esforco_momento(E, I, n, nodes, weights, cargas):
    x = np.linspace(0, L, 100)
    y = [calc_esforco_momento(E, I, n, nodes, weights, cargas)[i][0] for i in range(n+1)]

    plt.plot(x, y)
    plt.xlabel('Posição (m)')
    plt.ylabel('Esforço Cortante (N)')
    plt.title('Esforço Cortante x Posição')
    plt.show()

    plt.plot(x, y)
    plt.xlabel('Posição (m)')
    plt.ylabel('Momento Fletor (N*m)')
    plt.title('Momento Fletor x Posição')
    plt.show()

# Calcula e imprime os resultados
calc_esforco_momento(E, I, n, nodes, weights, cargas)
plot_esforco_momento(E, I, n, nodes, weights, cargas)