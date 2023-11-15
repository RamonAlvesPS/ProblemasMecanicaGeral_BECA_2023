from time import sleep
import Beam

# Inicializando variáveis
nome = "VigaSemNome"
tamanho = 0.0
apoios = []
cargas = []
momentos = []

def menu():
    print(
        """
		====================================================================
		||           <<<===>>> Calculadora de Vigas <<<===>>>             ||
		||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||
		||            <<<===>>> DR , DEC & DMF <<<===>>>                  ||
		====================================================================
        """
    )
    sleep(1)

    while True:
        print("\n	Informe o número correspondente para a opção desejada: ")
        print("	(1) Adicionar Informações da Viga;")
        print("	(2) Mostrar Resumo das Informações da Viga;")
        print("	(3) Mostrar Diagrama de Reações;")
        print("	(4) Mostrar Diagrama de Esforço Cortante;")
        print("	(5) Mostrar Diagrama de Momento Fletor;")
        print("	(6) Mostrar Todos os Diagramas (sequencialmente);")
        print("	(0) Para Encerrar;")
        op = int(input(">>> "))

        if op not in range(7):
            print("\n <|||> ERRO: opção inválida... <|||>")
            sleep(2)
            exit()

        elif op == 1:
            informacoesViga()

        elif op == 2:
            resumoViga()

        elif op == 3:
            diagramaReacao()

        elif op == 4:
            diagramaEsforcoCortante()
        
        elif op == 5:
            diagramaMomentoFletor()
        
        elif op == 6:
            todosDiagramas()

        elif op == 0:
            print("	Obg por usar nosso Código! ")
            sleep(0.5)
            print("			< by Alunos de BECA - IFPBcz - 2023 > ")
            sleep(0.5)
            exit()

def informacoesViga():
    global nome, tamanho, apoios, cargas, momentos

    nome = input("Nome da Viga: ")

    tamanho = float(input("Comprimento total da viga (m): "))

    quantidade_apoios = int(input("Quantidade de apoios: "))

    for i in range(quantidade_apoios):
        tipo_apoio = input(f"O tipo do apoio {i+1} (pino, rolete ou engaste): ").lower()
        posicao_apoio = float(input(f"Digite a posição do apoio {i+1} (m): "))

        if tipo_apoio not in ["pino", "rolete", "engaste"]:
            print("Tipo de apoio inválido. Use 'pino', 'rolete' ou 'engaste'.")
            sleep(2)
            informacoesViga()

        apoios.append({"Apoio": i+1, "Tipo": tipo_apoio, "Posicao": posicao_apoio})

    quantidade_cargas = int(input("Informe a quantidade de cargas: "))

    for i in range(quantidade_cargas):
        tipo_carga = input("Informe o tipo de carga (momento, pontual ou distribuida): ").lower()

        if tipo_carga == "momento":
            posicao_carga = float(input(f'Informe a posição do Momento {i+1} (m): '))
            valor_carga = float(input(f'Informe o valor do Momento {i+1} (kN/m): '))
            momentos.append({"Momento": i+1, "Posicao": posicao_carga, "Valor": valor_carga})

        elif tipo_carga == "pontual":
            posicao_carga = float(input(f'Informe a posição da carga pontual {i+1} (m): '))
            valor_carga = float(input(f'Informe o valor da carga pontual {i+1} (kN): '))
            cargas.append({"Tipo": tipo_carga, "Posicao": posicao_carga, "Valor": valor_carga})

        elif tipo_carga == "distribuida":
            posicao_inicial = float(input(f'Informe a posição inicial da carga distribuída {i+1} (m): '))
            posicao_final = float(input(f'Informe a posição final da carga distribuída {i+1} (m): '))
            valor_inicial = float(input(f'Informe o valor inicial da carga distribuída {i+1} (kN): '))
            valor_final = float(input(f'Informe o valor final da carga distribuída {i+1} (kN): '))
            cargas.append({"Tipo": tipo_carga, "PosicaoInicial": posicao_inicial, "PosicaoFinal": posicao_final, "ValorInicial": valor_inicial, "ValorFinal": valor_final})

    print("Informações da viga adicionadas com sucesso!")

def resumoViga():
    global nome, tamanho, apoios, cargas, momentos

    if tamanho <= 0:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que você não colocou o comprimento da Viga corretamente.")
        sleep(0.5)
        print("Por favor, reinicie o programa!")
        sleep(1)
        exit()

    viga = Beam.beam(str(nome), 0.5, 0.25, float(tamanho))

    for apoio in apoios:
        tipo_apoio = apoio['Tipo']
        posicao_apoio = apoio['Posicao']
        viga.add_point_support(float(posicao_apoio), 5, int(tipo_apoio))

    for carga in cargas:
        tipo_carga = carga['Tipo']
        if tipo_carga == "momento":
            posicao_carga = carga['Posicao']
            valor_carga = carga['Valor']
            viga.add_pure_bending_moment(float(posicao_carga), float(valor_carga))
        elif tipo_carga == "pontual":
            posicao_carga = carga['Posicao']
            valor_carga = carga['Valor']
            viga.add_point_load(float(posicao_carga), float(valor_carga))
        elif tipo_carga == "distribuida":
            posicao_inicial = carga['PosicaoInicial']
            posicao_final = carga['PosicaoFinal']
            valor_inicial = carga['ValorInicial']
            valor_final = carga['ValorFinal']
            viga.add_distributed_load(float(posicao_inicial), float(posicao_final), float(valor_inicial), float(valor_final))

    viga.analyze()

    print("\nResumo da Viga:")
    print(viga)

def diagramaReacao():
    global nome, tamanho, apoios, cargas, momentos

    if tamanho <= 0:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que você não colocou o comprimento da Viga corretamente.")
        sleep(0.5)
        print("Por favor, reinicie o programa!")
        sleep(1)
        exit()

    viga = Beam.beam(str(nome), 0.5, 0.25, float(tamanho))

    for apoio in apoios:
        tipo_apoio = apoio['Tipo']
        posicao_apoio = apoio['Posicao']
        viga.add_point_support(float(posicao_apoio), 5, int(tipo_apoio))

    for carga in cargas:
        tipo_carga = carga['Tipo']
        if tipo_carga == "momento":
            posicao_carga = carga['Posicao']
            valor_carga = carga['Valor']
            viga.add_pure_bending_moment(float(posicao_carga), float(valor_carga))
        elif tipo_carga == "pontual":
            posicao_carga = carga['Posicao']
            valor_carga = carga['Valor']
            viga.add_point_load(float(posicao_carga), float(valor_carga))
        elif tipo_carga == "distribuida":
            posicao_inicial = carga['PosicaoInicial']
            posicao_final = carga['PosicaoFinal']
            valor_inicial = carga['ValorInicial']
            valor_final = carga['ValorFinal']
            viga.add_distributed_load(float(posicao_inicial), float(posicao_final), float(valor_inicial), float(valor_final))

    viga.analyze()
    viga.calculate_reaction()

    print("\nDiagrama de Reações:")
    viga.show_reaction_force_diagram()

def diagramaEsforcoCortante():
    global nome, tamanho, apoios, cargas, momentos

    if tamanho <= 0:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que você não colocou o comprimento da Viga corretamente.")
        sleep(0.5)
        print("Por favor, reinicie o programa!")
        sleep(1)
        exit()

    viga = Beam.beam(str(nome), 0.5, 0.25, float(tamanho))

    for apoio in apoios:
        tipo_apoio = apoio['Tipo']
        posicao_apoio = apoio['Posicao']
        viga.add_point_support(float(posicao_apoio), 5, int(tipo_apoio))

    for carga in cargas:
        tipo_carga = carga['Tipo']
        if tipo_carga == "momento":
            posicao_carga = carga['Posicao']
            valor_carga = carga['Valor']
            viga.add_pure_bending_moment(float(posicao_carga), float(valor_carga))
        elif tipo_carga == "pontual":
            posicao_carga = carga['Posicao']
            valor_carga = carga['Valor']
            viga.add_point_load(float(posicao_carga), float(valor_carga))
        elif tipo_carga == "distribuida":
            posicao_inicial = carga['PosicaoInicial']
            posicao_final = carga['PosicaoFinal']
            valor_inicial = carga['ValorInicial']
            valor_final = carga['ValorFinal']
            viga.add_distributed_load(float(posicao_inicial), float(posicao_final), float(valor_inicial), float(valor_final))

    viga.analyze()
    viga.calculate_shear_force()

    print("\nDiagrama de Esforço Cortante:")
    viga.show_shear_force_diagram()

def diagramaMomentoFletor():
    global nome, tamanho, apoios, cargas, momentos

    if tamanho <= 0:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que você não colocou o comprimento da Viga corretamente.")
        sleep(0.5)
        print("Por favor, reinicie o programa!")
        sleep(1)
        exit()

    viga = Beam.beam(str(nome), 0.5, 0.25, float(tamanho))

    for apoio in apoios:
        tipo_apoio = apoio['Tipo']
        posicao_apoio = apoio['Posicao']
        viga.add_point_support(float(posicao_apoio), 5, int(tipo_apoio))

    for carga in cargas:
        tipo_carga = carga['Tipo']
        if tipo_carga == "momento":
            posicao_carga = carga['Posicao']
            valor_carga = carga['Valor']
            viga.add_pure_bending_moment(float(posicao_carga), float(valor_carga))
        elif tipo_carga == "pontual":
            posicao_carga = carga['Posicao']
            valor_carga = carga['Valor']
            viga.add_point_load(float(posicao_carga), float(valor_carga))
        elif tipo_carga == "distribuida":
            posicao_inicial = carga['PosicaoInicial']
            posicao_final = carga['PosicaoFinal']
            valor_inicial = carga['ValorInicial']
            valor_final = carga['ValorFinal']
            viga.add_distributed_load(float(posicao_inicial), float(posicao_final), float(valor_inicial), float(valor_final))

    viga.analyze()
    viga.calculate_bending_moment()

    print("\nDiagrama de Momento Fletor:")
    viga.show_bending_moment_diagram()

def todosDiagramas():
    diagramaReacao()
    diagramaEsforcoCortante()
    diagramaMomentoFletor()

if __name__ == "__main__":
    menu()
