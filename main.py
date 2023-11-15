#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Essas duas linhas são comentários especiais usados para configurar o ambiente de execução do código.

from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

from time import sleep
import Beam

# ==========    Iniciando variaveis     ==========
nome = "VigaSemNome" # Noem da viga
tamanho = float() # Comprimento total da viga
quantidade_apoios = int() # Ler o Quantidade de apoios
apoios = [] # Armazena as posições dos nós
tipo_apoio = float()
posicao_apoio = float()
apoio = {"Apoio": quantidade_apoios, "Tipo": tipo_apoio, "Posicao": posicao_apoio} # Armazena os valores em um dicionário
apoios.append(apoio) # Adiciona o dicionário à lista de apoios
quantidade_cargas = int() # Solicita a quantidade de cargas do usuário
cargas = [] # Lista para armazenar as informações das cargas
tipo_carga = ("tipo").lower() # Solicita o tipo de carga ao usuário
posicao = float()
valor = float()
carga = {"Tipo": tipo_carga, "Posicao": posicao, "Valor": valor}
posicao_inicial = float()
posicao_final = float()
valor_inicial = float()
valor_final = float()
carga = {"Tipo": tipo_carga, "PosicaoInicial": posicao_inicial, "PosicaoFinal": posicao_final, "ValorInicial": valor_inicial, "ValorFinal": valor_final}
cargas.append(carga)
quantidade_momentos = 0
momentos = []
posicao_momento = 0
valor_momento = 0

def menu():  # A função main() é a função principal que organiza a execução do programa.
    control = True

    print(
        f"""
		{Fore.RED}====================================================================
		||{Fore.GREEN}           <<<===>>> Calculadora de Vigas <<<===>>>             {Fore.RED}||
		||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||
		||{Fore.GREEN}            <<<===>>> DR , DEC & DMF <<<===>>>                  {Fore.RED}||
		====================================================================
        """
    )
    sleep(1)

    while control == True:
        print(f"{Fore.CYAN}\n	Informe o número correspondente para a opção desejada: {Style.RESET_ALL}")
        print("	(1) Adicionar Informações da Viga;")
        print("	(2) Mostrar Resumo das Informações da Viga;")
        print("	(3) Mostrar Diagrama de Reações;")
        print("	(4) Mostrar Diagrama de Esforço Cortante;")
        print("	(5) Mostrar Diagrama de Momento Fletor;")
        print("	(6) Mostrar Todos Diagramas (sequencialmente...);")
        print("	(0) Para Encerrar;")
        op = int(input(">>> "))

        if (op < 0) or (op > 6):  # Caso a opção informada seja invalida
            print(f"{Fore.RED}\n <|||> ERRO: opção invalida... <|||> \n  **Por favor, reinicie o programa e informe uma opção valida...{Style.RESET_ALL}")
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

        elif (op == 0) or (i == False):  # Encerra o programa
            sleep(0.5)
            print(f'{Fore.MAGENTA}	Obg por usar nosso Código! {Style.RESET_ALL}')
            sleep(0.5)
            print(f'{Fore.GREEN}			< by Alunos de BECA - IFPBcz - 2023 > {Style.RESET_ALL}')
            sleep(0.5)
            # break
            exit()

def informacoesViga():
    control = True
    print(
        """
		====================================================================
		||          <<<===>>> Inserir informações da Viga <<<===>>>       ||
		====================================================================
        """
    )
    sleep(1)

    while control == True:
        print("\n	Por favor, digite o número correspondente à informação que deseja inserir: ")
        print("	(1) Nome;")
        print("	(2) Comprimento total;")
        print("	(3) Apoio(s);")
        print("	(4) Carga(s);")
        print("	(5) Momento(s);")
        print("	(0) Voltar para o MENU;")
        op = int(input(">>> "))

        if (op < 0) or (op > 5):  # Caso a opção informada seja invalida
            print(
                "\n <|||> ERRO: opção invalida... <|||> \n  **Por favor, reinicie o programa e informe uma opção valida..."
            )
            exit()

        elif op == 1:
            global nome
            nome = input("Nome da Viga: ")
        
        elif op == 2:
            global tamanho
            tamanho = float(input("Comprimento total da viga (m): ")) # Ler o comprimento total da viga
        
        elif op == 3:
            global quantidade_apoios, apoio, tipo_apoio, posicao_apoio, apoio, apoios
            quantidade_apoios = int(input("Quantidade de apoios: ")) # Ler o Quantidade de apoios
            apoios = [] # Armazena as posições dos nós

            for i in range(quantidade_apoios):
                tipo_apoio = input(f"O tipo do apoio {i+1} (pino, rolete ou engaste): ").lower()

                if tipo_apoio == "pino":
                    tipo_apoio = 2
                elif tipo_apoio == "rolete":
                    tipo_apoio = 1
                elif tipo_apoio == "engaste":
                    tipo_apoio = 3
                else:
                    print("Tipo de apoio inválido. Use 'pino', 'rolete' ou 'engaste'.")
                    sleep(2)
                    informacoesViga()
                
                posicao_apoio = float(input(f"Digite a posição apoio {i+1} (m): "))
                apoio = {"Apoio": i+1, "Tipo": tipo_apoio, "Posicao": posicao_apoio} # Armazena os valores em um dicionário
                apoios.append(apoio) # Adiciona o dicionário à lista de apoios
        
        elif op == 4:
            global quantidade_cargas, cargas, tipo_carga, posicao, valor, carga, cargas, posicao_inicial, posicao_final, valor_inicial, valor_final
            quantidade_cargas = int(input("Informe a quantidade de cargas: ")) # Solicita a quantidade de cargas do usuário
            cargas = [] # Lista para armazenar as informações das cargas

            for i in range(1, quantidade_cargas + 1): # Loop para obter informações para cada carga
                print(f"\nCarga {i}:")
                tipo_carga = input("Informe o tipo de carga (pontual ou distribuida): ").lower() # Solicita o tipo de carga ao usuário
                
                # Verifica o tipo de carga e solicita informações relevantes
                if tipo_carga in ["pontual"]:
                    posicao = float(input("Informe a posição da carga (m): "))
                    valor = float(input("Informe o valor da carga (kN): "))
                    carga = {"Tipo": tipo_carga, "Posicao": posicao, "Valor": valor}
                elif tipo_carga == "distribuida":
                    posicao_inicial = float(input("Informe a posição inicial da carga distribuída (m): "))
                    posicao_final = float(input("Informe a posição final da carga distribuída (m): "))
                    valor_inicial = float(input("Informe o valor inicial da carga distribuída (kN): "))
                    valor_final = float(input("Informe o valor final da carga distribuída (kN): "))
                    carga = {"Carga": i+1, "Tipo": tipo_carga, "PosicaoInicial": posicao_inicial, "PosicaoFinal": posicao_final, "ValorInicial": valor_inicial, "ValorFinal": valor_final}
                else:
                    print("Tipo de carga inválido. Use 'momento', 'pontual' ou 'distribuida'.")
                    sleep(2)
                    informacoesViga()
                cargas.append(carga) # Adiciona o dicionário à lista de cargas
        
        elif op == 5:
            global quantidade_momentos, momentos, posicao_momento, valor_momento
            quantidade_momentos = int(input("Informe a quantidade de momentos: ")) # Solicita a quantidade de momentos do usuário
            momentos = [] # Lista para armazenar as informações das momentos

            for i in range(1, quantidade_momentos + 1): # Loop para obter informações para cada carga
                print(f"\nMomento {i}:")
                posicao = float(input(f'Informe a posição do Momento {i} (m): '))
                valor = float(input(f'Informe o valor do Momento {i} (kN/m): '))
                momento = {"Momento": i, "Posicao": posicao, "Valor": valor}
                momentos.append(momento) # Adiciona o dicionário à lista de momentos


        elif (op == 0) or (i == False):
            menu()

def resumoViga():

    if tamanho > 0:
        viga = Beam.beam(str(nome),0.5,0.25,float(tamanho))
        # print(f'viga = Beam.beam({str(nome)}, 0.5, 0.25, {tamanho})')
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o comprimento da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()

    if quantidade_apoios > 0:
        for apoio in apoios:
            tipo_apoio = apoio['Tipo']
            posicao_apoio = apoio['Posicao']
            viga.add_point_support(float(posicao_apoio),5,int(tipo_apoio))
            # print(f'viga.add_point_support({posicao_apoio}, 5, {tipo_apoio})')
    elif quantidade_apoios == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Apoios da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()
    
    if quantidade_cargas > 0:
        for carga in cargas:
            tipo_carga = carga['Tipo']
            if tipo_carga == "momento":
                posicao_carga = carga['Posicao']
                valor_carga = carga['Valor']
                # viga.add_pure_bending_moment(float(posicao_carga),float(valor_carga))
                print(f'viga.add_pure_bending_moment({posicao_carga},{valor_carga})')
            elif tipo_carga == "pontual":
                posicao_carga = carga['Posicao']
                valor_carga = carga['Valor']
                # viga.add_point_load(float(posicao_carga), float(valor_carga))
                print(f'viga.add_point_load({posicao_carga}, {valor_carga})')
            elif tipo_carga == "distribuida":
                posicao_inicial = carga['PosicaoInicial']
                posicao_final = carga['PosicaoFinal']
                valor_inicial = carga['ValorInicial']
                valor_final = carga['ValorFinal']
                viga.add_distributed_load([float(posicao_inicial), float(posicao_final)], [float(valor_inicial), float(valor_final)])                
                # print(f'viga.add_distributed_load([{posicao_inicial}, {posicao_final}], [{valor_inicial}, {valor_final}])')
    elif quantidade_cargas == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Cargas da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()

    if quantidade_momentos > 0:
        for momento in momentos:
            posicao_carga = carga['Posicao']
            valor_carga = carga['Valor']
            viga.add_pure_bending_moment(float(posicao_carga),float(valor_carga))
            # print(f'viga.add_pure_bending_moment({posicao_carga},{valor_carga})')  
    elif quantidade_momentos == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Momentos da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()          
    
    viga.info_beam()
    sleep(1)

def diagramaReacao():
    if tamanho > 0:
        viga = Beam.beam(str(nome),0.5,0.25,float(tamanho))
        # print(f'viga = Beam.beam({str(nome)}, 0.5, 0.25, {tamanho})')
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o comprimento da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()

    if quantidade_apoios > 0:
        for apoio in apoios:
            tipo_apoio = apoio['Tipo']
            posicao_apoio = apoio['Posicao']
            viga.add_point_support(float(posicao_apoio),5,int(tipo_apoio))
            # print(f'viga.add_point_support({posicao_apoio}, 5, {tipo_apoio})')
    elif quantidade_apoios == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Apoios da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()
    
    if quantidade_cargas > 0:
        for carga in cargas:
            tipo_carga = carga['Tipo']
            if tipo_carga == "momento":
                posicao_carga = carga['Posicao']
                valor_carga = carga['Valor']
                # viga.add_pure_bending_moment(float(posicao_carga),float(valor_carga))
                print(f'viga.add_pure_bending_moment({posicao_carga},{valor_carga})')
            elif tipo_carga == "pontual":
                posicao_carga = carga['Posicao']
                valor_carga = carga['Valor']
                # viga.add_point_load(float(posicao_carga), float(valor_carga))
                print(f'viga.add_point_load({posicao_carga}, {valor_carga})')
            elif tipo_carga == "distribuida":
                posicao_inicial = carga['PosicaoInicial']
                posicao_final = carga['PosicaoFinal']
                valor_inicial = carga['ValorInicial']
                valor_final = carga['ValorFinal']
                viga.add_distributed_load([float(posicao_inicial), float(posicao_final)], [float(valor_inicial), float(valor_final)])                
                # print(f'viga.add_distributed_load([{posicao_inicial}, {posicao_final}], [{valor_inicial}, {valor_final}])')
    elif quantidade_cargas == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Cargas da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()

    if quantidade_momentos > 0:
        for momento in momentos:
            posicao_carga = carga['Posicao']
            valor_carga = carga['Valor']
            viga.add_pure_bending_moment(float(posicao_carga),float(valor_carga))
            # print(f'viga.add_pure_bending_moment({posicao_carga},{valor_carga})')  
    elif quantidade_momentos == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Momentos da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()          
    
    viga.plot_load()

def diagramaEsforcoCortante():
    if tamanho > 0:
        viga = Beam.beam(str(nome),0.5,0.25,float(tamanho))
        # print(f'viga = Beam.beam({str(nome)}, 0.5, 0.25, {tamanho})')
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o comprimento da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()

    if quantidade_apoios > 0:
        for apoio in apoios:
            tipo_apoio = apoio['Tipo']
            posicao_apoio = apoio['Posicao']
            viga.add_point_support(float(posicao_apoio),5,int(tipo_apoio))
            # print(f'viga.add_point_support({posicao_apoio}, 5, {tipo_apoio})')
    elif quantidade_apoios == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Apoios da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()
    
    if quantidade_cargas > 0:
        for carga in cargas:
            tipo_carga = carga['Tipo']
            if tipo_carga == "momento":
                posicao_carga = carga['Posicao']
                valor_carga = carga['Valor']
                # viga.add_pure_bending_moment(float(posicao_carga),float(valor_carga))
                print(f'viga.add_pure_bending_moment({posicao_carga},{valor_carga})')
            elif tipo_carga == "pontual":
                posicao_carga = carga['Posicao']
                valor_carga = carga['Valor']
                # viga.add_point_load(float(posicao_carga), float(valor_carga))
                print(f'viga.add_point_load({posicao_carga}, {valor_carga})')
            elif tipo_carga == "distribuida":
                posicao_inicial = carga['PosicaoInicial']
                posicao_final = carga['PosicaoFinal']
                valor_inicial = carga['ValorInicial']
                valor_final = carga['ValorFinal']
                viga.add_distributed_load([float(posicao_inicial), float(posicao_final)], [float(valor_inicial), float(valor_final)])                
                # print(f'viga.add_distributed_load([{posicao_inicial}, {posicao_final}], [{valor_inicial}, {valor_final}])')
    elif quantidade_cargas == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Cargas da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()

    if quantidade_momentos > 0:
        for momento in momentos:
            posicao_carga = carga['Posicao']
            valor_carga = carga['Valor']
            viga.add_pure_bending_moment(float(posicao_carga),float(valor_carga))
            # print(f'viga.add_pure_bending_moment({posicao_carga},{valor_carga})')  
    elif quantidade_momentos == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Momentos da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()          
    
    viga.plot_shear()

def diagramaMomentoFletor():
    if tamanho > 0:
        viga = Beam.beam(str(nome),0.5,0.25,float(tamanho))
        # print(f'viga = Beam.beam({str(nome)}, 0.5, 0.25, {tamanho})')
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o comprimento da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()

    if quantidade_apoios > 0:
        for apoio in apoios:
            tipo_apoio = apoio['Tipo']
            posicao_apoio = apoio['Posicao']
            viga.add_point_support(float(posicao_apoio),5,int(tipo_apoio))
            # print(f'viga.add_point_support({posicao_apoio}, 5, {tipo_apoio})')
    elif quantidade_apoios == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Apoios da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()
    
    if quantidade_cargas > 0:
        for carga in cargas:
            tipo_carga = carga['Tipo']
            if tipo_carga == "momento":
                posicao_carga = carga['Posicao']
                valor_carga = carga['Valor']
                # viga.add_pure_bending_moment(float(posicao_carga),float(valor_carga))
                print(f'viga.add_pure_bending_moment({posicao_carga},{valor_carga})')
            elif tipo_carga == "pontual":
                posicao_carga = carga['Posicao']
                valor_carga = carga['Valor']
                # viga.add_point_load(float(posicao_carga), float(valor_carga))
                print(f'viga.add_point_load({posicao_carga}, {valor_carga})')
            elif tipo_carga == "distribuida":
                posicao_inicial = carga['PosicaoInicial']
                posicao_final = carga['PosicaoFinal']
                valor_inicial = carga['ValorInicial']
                valor_final = carga['ValorFinal']
                viga.add_distributed_load([float(posicao_inicial), float(posicao_final)], [float(valor_inicial), float(valor_final)])                
                # print(f'viga.add_distributed_load([{posicao_inicial}, {posicao_final}], [{valor_inicial}, {valor_final}])')
    elif quantidade_cargas == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Cargas da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()

    if quantidade_momentos > 0:
        for momento in momentos:
            posicao_carga = carga['Posicao']
            valor_carga = carga['Valor']
            viga.add_pure_bending_moment(float(posicao_carga),float(valor_carga))
            # print(f'viga.add_pure_bending_moment({posicao_carga},{valor_carga})')  
    elif quantidade_momentos == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Momentos da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()          
    
    viga.info_beam()

def todosDiagramas():
    if tamanho > 0:
        viga = Beam.beam(str(nome),0.5,0.25,float(tamanho))
        # print(f'viga = Beam.beam({str(nome)}, 0.5, 0.25, {tamanho})')
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o comprimento da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()

    if quantidade_apoios > 0:
        for apoio in apoios:
            tipo_apoio = apoio['Tipo']
            posicao_apoio = apoio['Posicao']
            viga.add_point_support(float(posicao_apoio),5,int(tipo_apoio))
            # print(f'viga.add_point_support({posicao_apoio}, 5, {tipo_apoio})')
    elif quantidade_apoios == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Apoios da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()
    
    if quantidade_cargas > 0:
        for carga in cargas:
            tipo_carga = carga['Tipo']
            if tipo_carga == "momento":
                posicao_carga = carga['Posicao']
                valor_carga = carga['Valor']
                # viga.add_pure_bending_moment(float(posicao_carga),float(valor_carga))
                print(f'viga.add_pure_bending_moment({posicao_carga},{valor_carga})')
            elif tipo_carga == "pontual":
                posicao_carga = carga['Posicao']
                valor_carga = carga['Valor']
                # viga.add_point_load(float(posicao_carga), float(valor_carga))
                print(f'viga.add_point_load({posicao_carga}, {valor_carga})')
            elif tipo_carga == "distribuida":
                posicao_inicial = carga['PosicaoInicial']
                posicao_final = carga['PosicaoFinal']
                valor_inicial = carga['ValorInicial']
                valor_final = carga['ValorFinal']
                viga.add_distributed_load([float(posicao_inicial), float(posicao_final)], [float(valor_inicial), float(valor_final)])                
                # print(f'viga.add_distributed_load([{posicao_inicial}, {posicao_final}], [{valor_inicial}, {valor_final}])')
    elif quantidade_cargas == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Cargas da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()

    if quantidade_momentos > 0:
        for momento in momentos:
            posicao_carga = carga['Posicao']
            valor_carga = carga['Valor']
            viga.add_pure_bending_moment(float(posicao_carga),float(valor_carga))
            # print(f'viga.add_pure_bending_moment({posicao_carga},{valor_carga})')  
    elif quantidade_momentos == 0: pass
    else:
        print("Opah!! Algo de errado não está certo...")
        sleep(0.5)
        print("Acho que vc não colocou o a quantidade de Momentos da Viga corretamente.")
        sleep(0.5)
        print("PorFavor, reinicie o programa!")
        sleep(1)
        exit()

    viga.info_beam()

    viga.plot_load()
    viga.plot_shear()
    viga.plot_moment()

if __name__ == "__main__":
    menu()