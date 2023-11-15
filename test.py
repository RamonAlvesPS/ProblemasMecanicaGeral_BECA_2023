# Entrada de dados

"""
n = int(input('Quantidade de nós: '))
#n_list = list(map(float, input('Posições dos nós (ex: 1 3 5): ').split()))
n_list = list(map(float, input('Posições dos nós (ex: 1 3 5): ').split(", ")))

print(n_list)
print(n_list[0])
print(n_list[1])
print(n_list[2])
print(n_list[3])

"""
def Apoios():
        
    a = int(input("Quantidade de apoios: ")) # Ler o Quantidade de apoios
    apoios = [] # Armazena as posições dos nós

    for i in range(a):
        tipo = float(input(f"O tipo do apoio {i+1}: "))
        posicao = float(input(f"Digite a posição apoio {i+1}: "))

        # Armazena os valores em um dicionário
        apoio = {"Apoio": i, "Tipo": tipo, "Posicao": posicao}
        
        # Adiciona o dicionário à lista de apoios
        apoios.append(apoio)

    # Exibe os resultados
    print("\nValores dos apoios:")
    for apoio in apoios:
        print(f"Apoio {apoio['Apoio']}: Valor1 = {apoio['Tipo']}, Valor2 = {apoio['Posicao']}")

def Cargas():
    # Solicita a quantidade de cargas do usuário
    quantidade_cargas = int(input("Informe a quantidade de cargas: "))

    # Lista para armazenar as informações das cargas
    cargas = []

    # Loop para obter informações para cada carga
    for i in range(1, quantidade_cargas + 1):
        print(f"\nCarga {i}:")
        
        # Solicita o tipo de carga ao usuário
        tipo_carga = input("Informe o tipo de carga (momento, pontual ou distribuida): ").lower()
        
        # Verifica o tipo de carga e solicita informações relevantes
        if tipo_carga in ["momento"]:
            posicao = float(input("Informe a posição da carga (m): "))
            valor = float(input("Informe o valor da carga (kN/m): "))
            carga = {"Tipo": tipo_carga, "Posicao": posicao, "Valor": valor}
        if tipo_carga in ["pontual"]:
            posicao = float(input("Informe a posição da carga (m): "))
            valor = float(input("Informe o valor da carga (kN): "))
            carga = {"Tipo": tipo_carga, "Posicao": posicao, "Valor": valor}
        elif tipo_carga == "distribuida":
            posicao_inicial = float(input("Informe a posição inicial da carga distribuída: "))
            posicao_final = float(input("Informe a posição final da carga distribuída: "))
            valor_inicial = float(input("Informe o valor inicial da carga distribuída: "))
            valor_final = float(input("Informe o valor final da carga distribuída: "))
            carga = {"Tipo": tipo_carga, "PosicaoInicial": posicao_inicial, "PosicaoFinal": posicao_final, "ValorInicial": valor_inicial, "ValorFinal": valor_final}
        else:
            print("Tipo de carga inválido. Use 'momento', 'pontual' ou 'distribuida'.")
            # continue
            i = i - 2
        
        # Adiciona o dicionário à lista de cargas
        cargas.append(carga)

    # Exibe os resultados
    print("\nInformações das cargas:")
    for carga in cargas:
        print(f"\nTipo: {carga['Tipo']}")
        if carga['Tipo'] in ["momento", "pontual"]:
            print(f"Posição: {carga['Posicao']}, Valor: {carga['Valor']}")
        elif carga['Tipo'] == "distribuida":
            print(f"Posição Inicial: {carga['PosicaoInicial']}, Posição Final: {carga['PosicaoFinal']}")
            print(f"Valor Inicial: {carga['ValorInicial']}, Valor Final: {carga['ValorFinal']}")

Cargas()