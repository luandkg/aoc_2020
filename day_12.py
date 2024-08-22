def main():

    ADVENT_PROJETO = "2020"
    ADVENT_OF_CODE = "12"
    DATA_DA_RESOLUCAO = "2024 08 21"


    print("")
    print("---------- Advent of Code " + ADVENT_OF_CODE + " --------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : "+DATA_DA_RESOLUCAO)
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """F10
N3
F7
R90
F11"""
    solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    solucao(transformar_texto_em_entradas(obter_entradas("inputs/input_" + ADVENT_OF_CODE + ".txt")))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")

    entrada_texto ="""F10
N3
F7
R90
F11"""

    solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    solucao_parte_extra(transformar_texto_em_entradas(obter_entradas("inputs/input_" + ADVENT_OF_CODE + ".txt")))


def transformar_texto_em_entradas(entrada_texto):
    entradas = []
    for linha in entrada_texto.split("\n"):
        if(len(linha)>0):
            entradas.append(linha)
    return entradas

def obter_entradas(arquivo_caminho):
    
    texto = ""

    arquivo = open(arquivo_caminho)
    for linha in arquivo.readlines():
        texto = texto + linha

    return texto


def solucao(entradas):

    direcoes = ["N","S","E","W","L","R","F"]

    NORTH_SOUTH = 0
    EAST_WEST   = 0
    DIRECTION = direcoes[2]

    print("Iniciando percurso em Manhattan : ")
    print()
    print("\t -->> " + DIRECTION)
    print()

    direcionadores = {"N":"NORTH","S":"SOUTH","E":"EAST","W":"WEST"}
    valores = {"NORTH":0,"SOUTH":0,"EAST":0,"WEST":0}

    DIRECOES = ["N","E","S","W"]

    executando = 0

    for entrada in entradas:

        ir_para = entrada[0]
        ir_quantidade = int(entrada[1:])
        print("\t ++ Entrada : " + espacar(entrada,10) + " :: " + ir_para + " :: " + str(ir_quantidade))

        if ir_para == "F":
            valores[direcionadores[DIRECTION]] +=ir_quantidade
        elif ir_para == "N" or ir_para == "E" or ir_para == "S" or ir_para == "W":
            valores[direcionadores[ir_para]] +=ir_quantidade
        elif ir_para == "R":
            print("Estou em :: " + DIRECTION)
            de = obter_direcao(DIRECTION,DIRECOES)
            alterar = int(ir_quantidade / 90)
            nova_direcao = (de + alterar) % 4
           
            DIRECTION = DIRECOES[nova_direcao]
            print("Mudar :: " + str(de) + " com " + str(alterar) + " = " + str(nova_direcao) + " -->> " + DIRECTION)
        elif ir_para == "L":
            print("Estou em :: " + DIRECTION)
            de = obter_direcao(DIRECTION,DIRECOES)
            alterar = int(ir_quantidade / 90)
            nova_direcao = (de - alterar)  
            while nova_direcao<0:
                nova_direcao+=4
           
            DIRECTION = DIRECOES[nova_direcao]
            print("Mudar :: " + str(de) + " com " + str(alterar) + " = " + str(nova_direcao) + " -->> " + DIRECTION)


        NORTH_SOUTH = abs(int(valores["NORTH"]) - int(valores["SOUTH"]))
        EAST_WEST = abs(int(valores["EAST"]) - int(valores["WEST"]))

        print("\t\t :: DIR         = " + DIRECTION)
        print("\t\t :: NORTH_SOUTH = " + str(NORTH_SOUTH))
        print("\t\t :: EAST_WEST   = " + str(EAST_WEST))
        print("\t\t :: VALOR       = " + str(NORTH_SOUTH+EAST_WEST))

        executando+=1
        





def solucao_parte_extra(entradas):

    direcoes = ["N","S","E","W","L","R","F"]

    NORTH_SOUTH = 0
    EAST_WEST   = 0
    DIRECTION = direcoes[2]

    print("Iniciando percurso em Manhattan : ")
    print()
    print("\t -->> " + DIRECTION)
    print()

    direcionadores = {"N":"NORTH","S":"SOUTH","E":"EAST","W":"WEST"}
    unidades = {"NORTH":0,"SOUTH":0,"EAST":0,"WEST":0}
    waypoints = {"NORTH":1,"SOUTH":0,"EAST":10,"WEST":0}

    DIRECOES = ["N","E","S","W"]

    executando = 0

    for entrada in entradas:

        ir_para = entrada[0]
        ir_quantidade = int(entrada[1:])
        print("\t ++ Entrada : " + espacar(entrada,10) + " :: " + ir_para + " :: " + str(ir_quantidade))

        if ir_para == "F":
            #valores[direcionadores[DIRECTION]] +=ir_quantidade

            for direcao_alterar in DIRECOES:
                unidades[direcionadores[direcao_alterar]] +=(ir_quantidade*waypoints[direcionadores[direcao_alterar]]) 


        elif ir_para == "N" or ir_para == "E" or ir_para == "S" or ir_para == "W":
            waypoints[direcionadores[ir_para]] +=ir_quantidade
        elif ir_para == "R":
            print("Estou em :: " + DIRECTION)
            de = obter_direcao(DIRECTION,DIRECOES)
            alterar = int(ir_quantidade / 90)
            nova_direcao = (de + alterar) % 4
           
            DIRECTION = DIRECOES[nova_direcao]
            print("Mudar :: " + str(de) + " com " + str(alterar) + " = " + str(nova_direcao) + " -->> " + DIRECTION)

            waypoints_copia = {"NORTH":0,"SOUTH":0,"EAST":0,"WEST":0}

            for direcao_corrente in DIRECOES:
                waypoints_copia[direcionadores[direcao_corrente]] =  waypoints[direcionadores[direcao_corrente]]

            for direcao_corrente in DIRECOES:
                valor_direcao = waypoints_copia[direcionadores[direcao_corrente]]
                de = obter_direcao(direcao_corrente,DIRECOES)
                nova_direcao = (de + alterar) % 4
                waypoints[direcionadores[DIRECOES[nova_direcao]]] = valor_direcao

            

        elif ir_para == "L":
            print("Estou em :: " + DIRECTION)
            de = obter_direcao(DIRECTION,DIRECOES)
            alterar = int(ir_quantidade / 90)
            nova_direcao = (de - alterar)  
            while nova_direcao<0:
                nova_direcao+=4
           
            DIRECTION = DIRECOES[nova_direcao]
            print("Mudar :: " + str(de) + " com " + str(alterar) + " = " + str(nova_direcao) + " -->> " + DIRECTION)

            waypoints_copia = {"NORTH":0,"SOUTH":0,"EAST":0,"WEST":0}

            for direcao_corrente in DIRECOES:
                waypoints_copia[direcionadores[direcao_corrente]] =  waypoints[direcionadores[direcao_corrente]]

            for direcao_corrente in DIRECOES:
                valor_direcao = waypoints_copia[direcionadores[direcao_corrente]]
                de = obter_direcao(direcao_corrente,DIRECOES)
                nova_direcao = (de - alterar) % 4
                while nova_direcao<0:
                    nova_direcao+=4

                waypoints[direcionadores[DIRECOES[nova_direcao]]] = valor_direcao



        NORTH_SOUTH = abs(int(unidades["NORTH"]) - int(unidades["SOUTH"]))
        EAST_WEST = abs(int(unidades["EAST"]) - int(unidades["WEST"]))

        print("\t\t :: DIR         = " + DIRECTION)

        print("Unidades")
        for direcao_alterar in DIRECOES:
                valor_local = unidades[direcionadores[direcao_alterar]] 
                print("\t\t :: " + direcao_alterar + " :: " + str(valor_local))

        print("WayPoints")
        for direcao_alterar in DIRECOES:
                valor_local = waypoints[direcionadores[direcao_alterar]] 
                print("\t\t :: " + direcao_alterar + " :: " + str(valor_local))

        print()
        print("\t\t :: NORTH_SOUTH = " + str(NORTH_SOUTH))
        print("\t\t :: EAST_WEST   = " + str(EAST_WEST))
        print("\t\t :: VALOR       = " + str(NORTH_SOUTH+EAST_WEST))

        executando+=1
  


def espacar(s,tamanho):
    while len(s)<tamanho:
        s=s+" "

    return s

def obter_direcao(direcao,direcoes):

    valor =0
    for dir in direcoes:
        if dir == direcao:
            break
        valor+=1
    return valor

main()