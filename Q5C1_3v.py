# V 1.3

"""
Produza um Script em python que calcule e mostre o grafico do esforço cortante e momento fletor de uma viga dada pelo usuario. 
A viga terá um apoio fixo em X e Y no inicio do comprimento e um apoio fixo em Y e livre em X.
Além disso, a viga poderá ser informada de varia condições, por exemplo com nós (n) em diferentes posições de seu comprimento total (L), diferentes valores de pesos (W) em nós específicos, carga pontual, carga uniforme, carga linear...

"""

import numpy as np
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit
#from scipy.interpolate import interp1d

# Entrada de dados
E = float(input('Modulo de elasticidade [N/m^2]: '))
I = float(input('Momento de inércia [m^4]: '))
L = float(input('Comprimento da viga [m]: '))

n = int(input('Quantidade de nós: '))
n_list = list(map(float, input('Posições dos nós (ex: 1, 3.1, 5, 6.5)m: ').split(", ")))
W_list = list(map(float, input('Valores dos pesos (ex: 10 20 30)N: ').split()))

q_type = input('Tipo de carga (pontual, uniforme, linear): ')
q = float(input('Valor da carga [N]: '))

# Calculo do esforço cortante
def esforco_cortante(x):
    N = len(W_list)
    return np.sum([(n_list[i] + n_list[i+1])/2 * (W_list[i] + W_list[i+1])/2 for i in range(N-1)])

# Calculo do momento fletor
def momento_fletor(x):
    return q * x / L

# Calculo da derivada segunda do momento fletor
def momento_fletor_der2(x):
    return 0

# Calculo do esforço cortante real
def esforco_cortante_real(x):
    return esforco_cortante(x) - (momento_fletor(x) / (L * E * I)) * (L * L * L * L) / 12

# Calculo da deformação
def deformacao(x):
    return momentos_fletores(x) / (E * I)

# Calculo das rotações
def rotacoes(x):
    return momentos_fletores(x) / (L * E * I)

# Calculo dos deslocamentos
def deslocamentos(x):
    return rotacoes(x) * x / L

# Grafico do esforço cortante real e deformação
plt.figure(figsize=(10, 6))

x = np.linspace(0, L, 1000)
y_ec = esforco_cortante_real(x)
y_d = deformacao(x)

plt.plot(x, y_ec, label='Esforço Cortante Real')
plt.plot(x, y_d, label='Deformação')

plt.xlabel('Posição no elemento [m]')
plt.ylabel('Esforço [N/m^2] e Deformação [m]')
plt.title('Viga simplesmente apoiada com nós e pesos variáveis')
plt.legend()
plt.grid()
plt.show()

# Grafico do momento fletor e rotação
plt.figure(figsize=(10, 6))

x = np.linspace(0, L, 1000)
y_mf = momentos_fletores(x)
y_rot = rotacoes(x)

plt.plot(x, y_mf, label='Momento Fletor')
plt.plot(x, y_rot, label='Rotação')

plt.xlabel('Posição no elemento [m]')
plt.ylabel('Momento [Nm] e Rotação [rad]')
plt.title('Viga simplesmente apoiada com nós e pesos variáveis')
plt.legend()
plt.grid()
plt.show()

# Grafico do deslocamento e curva característica
plt.figure(figsize=(10, 6))

x = np.linspace(0, L, 1000)
y_d = deslocamentos(x)

plt.plot(x, y_d, label='Deslocamento')

# Curva característica
e = np.linspace(-1, 1, 1000)
w = (L * q * (1 - e**2)) / (2 * E * I)

plt.plot(e, w, label='Curva Característica')

plt.xlabel('Coeficiente de formato [-]')
plt.ylabel('Deslocamento [m] e Momento Fletor [Nm]')
plt.title('Viga simplesmente apoiada com nós e pesos variáveis')
plt.legend()
plt.grid()
plt.show()
