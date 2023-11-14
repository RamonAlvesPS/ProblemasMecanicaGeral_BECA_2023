import matplotlib.pyplot as plt

def calcular_esforco_cortante_momento_fletor(L, n, x, W, C):
    # Inicializar listas para armazenar os valores do esforço cortante e momento fletor
    esforco_cortante = []
    momento_fletor = []

    # Calcular o esforço cortante e momento fletor em cada ponto da viga
    for i in range(n):
        # Calcular o esforço cortante no ponto i
        cortante = sum(C[:i+1]) - sum(W[:i+1])
        esforco_cortante.append(cortante)

        # Calcular o momento fletor no ponto i
        momento = sum(C[:i+1]) * x[i] - sum(W[:i+1]) * (L - x[i])
        momento_fletor.append(momento)

    return esforco_cortante, momento_fletor

def plotar_grafico_viga(L, x, esforco_cortante, momento_fletor):
    plt.figure("Graficos DEC & DMF")
    
    # Plotar o gráfico do esforço cortante
    plt.subplot(2, 1, 1)
    plt.plot(x, esforco_cortante)
    plt.xlabel('Posição ao longo da viga (m)')
    plt.ylabel('Esforço Cortante (N)')
    plt.title('Esforço Cortante')

    # Plotar o gráfico do momento fletor
    plt.subplot(2, 1, 2)
    plt.plot(x, momento_fletor)
    plt.xlabel('Posição ao longo da viga (m)')
    plt.ylabel('Momento Fletor (Nm)')
    plt.title('Momento Fletor')

    # Exibir o gráfico
    plt.tight_layout()
    plt.show()

# Exemplo de uso
# L = 10  # Comprimento total da viga
# n = 5  # Número de nós
# x = [0, 2, 4, 6, 10]  # Posições dos nós
# W = [0, 10, 20, 15, 0]  # Valores dos pesos nos nós
# C = [0, 5, 10, 5, 0]  # Valores das cargas nos nós

L = 3  # Comprimento total da viga
n = 4  # Número de nós
x = [0, 0.90, 0.60, 1.5]  # Posições dos nós
W = [0, 0, 0, 0]  # Valores dos pesos nos nós
C = [0, 4.38, 4.38, 4.84]  # Valores das cargas nos nós

esforco_cortante, momento_fletor = calcular_esforco_cortante_momento_fletor(L, n, x, W, C)
plotar_grafico_viga(L, x, esforco_cortante, momento_fletor)