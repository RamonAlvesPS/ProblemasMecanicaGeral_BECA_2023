import matplotlib.pyplot as plt

# Subproblema 1: Ler as informações da viga fornecidas pelo usuário

# Ler o comprimento total da viga
L = float(input("Digite o comprimento total da viga: "))

# Ler o número de nós da viga
n = int(input("Digite o número de nós da viga: "))

# Criar uma lista para armazenar as posições dos nós
nos = []
for i in range(n):
    posicao = float(input(f"Digite a posição do nó {i+1}: "))
    nos.append(posicao)

# Ler as cargas aplicadas em cada nó
cargas = []
for i in range(n):
    carga = float(input(f"Digite a carga aplicada no nó {i+1}: "))
    cargas.append(carga)

# Ler o tipo de carga em cada nó
tipos_carga = []
for i in range(n):
    tipo = input(f"Digite o tipo de carga no nó {i+1} (pontual, uniforme, linear): ")
    tipos_carga.append(tipo)


# Subproblema 2: Calcular os esforços cortantes e momentos fletores em cada ponto da viga

# Inicializar as listas para armazenar os esforços cortantes e momentos fletores
esforco_cortante = []
momento_fletor = []

# Calcular os esforços cortantes e momentos fletores em cada ponto da viga
for i in range(n):
    # Calcular o esforço cortante no ponto
    cortante = sum(cargas[:i+1])
    esforco_cortante.append(cortante)

    # Calcular o momento fletor no ponto
    momento = sum(cargas[:i+1]) * nos[i]
    momento_fletor.append(momento)


# Subproblema 3: Plotar o gráfico dos esforços cortantes
plt.figure()
plt.plot(nos, esforco_cortante)
plt.xlabel('Posição (m)')
plt.ylabel('Esforço Cortante (N)')
plt.title('Gráfico do Esforço Cortante')
plt.grid(True)
plt.show()


# Subproblema 4: Plotar o gráfico dos momentos fletores
plt.figure()
plt.plot(nos, momento_fletor)
plt.xlabel('Posição (m)')
plt.ylabel('Momento Fletor (Nm)')
plt.title('Gráfico do Momento Fletor')
plt.grid(True)
plt.show()