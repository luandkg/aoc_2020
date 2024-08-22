def main():

    ADVENT_PROJETO = "2020"
    ADVENT_OF_CODE = "13"
    DATA_DA_RESOLUCAO = "2024 08 22"


    print("")
    print("---------- Advent of Code " + ADVENT_OF_CODE + " --------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : "+DATA_DA_RESOLUCAO)
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """939
7,13,x,x,59,x,31,19"""
    solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    solucao(transformar_texto_em_entradas(obter_entradas("inputs/input_" + ADVENT_OF_CODE + ".txt")))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")

    entrada_texto =""""""

    #solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    #solucao_parte_extra(transformar_texto_em_entradas(obter_entradas("inputs/input_" + ADVENT_OF_CODE + ".txt")))


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
    
    meu_horario = int(entradas[0])
    linha_completa = entradas[1]

    linhas = []
    horarios = []

    horario_iniciar = meu_horario-12
    horario_terminar = meu_horario+12

    i_horario = horario_iniciar
    while i_horario < horario_terminar:
        i_horario+=1
        horarios.append(i_horario)
    
    for linha in linha_completa.split(","):
        if(not linha == "x"):
            linhas.append(int(linha))

    cabecalho = "time   "
    for linha in linhas:
        cabecalho+=espacar("bus "+str(linha),10)

    print(cabecalho)

    itinerarios = []

    for horario_item in horarios:

        itinerario_corrente = []
        itinerario_corrente.append(horario_item)

        itinerario_horario = horario_item

        for itinerario_local in linhas:
            intervalo = itinerario_local

            itinerario_percorrendo = 0

            passa_aqui = False

            while itinerario_percorrendo <=itinerario_horario:
                if itinerario_percorrendo == itinerario_horario:
                    passa_aqui = True

                itinerario_percorrendo+=intervalo
                #print(">> " + str(itinerario_horario) + " - " + str(itinerario_percorrendo) )

            if passa_aqui:
                itinerario_corrente.append("D")
            else:
                itinerario_corrente.append(".")
        
        itinerarios.append(itinerario_corrente)


    itinerario_diferenca = 100_000_00
    itenerario_marcado = 100_000_000
    bus_id = 0
    itenerario_tempo=0
    
    
    for itinerario_corrente in itinerarios:
        itinerario_horario = itinerario_corrente[0]

        itinerario_status =espacar(str(itinerario_horario),10)

        tem_nesse = False
        tem_bus_id = 0

        for iti_id,itinerario_local in enumerate(itinerario_corrente):
            if iti_id > 0:
                if itinerario_local == "D":
                    tem_bus_id = iti_id - 1
                    tem_nesse = True
                    break


        for iti_id,itinerario_local in enumerate(itinerario_corrente):
            if iti_id > 0:

                if itinerario_local=="D":
                    itinerario_status+=espacar(str("D"),10)
                else:
                    itinerario_status+=espacar(str("."),10)

                if tem_nesse and itinerario_horario >= meu_horario:
                    localmente =itinerario_horario - meu_horario
                    if localmente < itinerario_diferenca:
                        itenerario_marcado = itinerario_horario
                        itinerario_diferenca = localmente



        
        if itenerario_marcado == itinerario_horario :
            bus_id = linhas[tem_bus_id]
            itenerario_tempo = itenerario_marcado - meu_horario
                    


        print(itinerario_status)

    
    itinerario_valor = itenerario_tempo * bus_id
    
    print("Itinerario Proximo : " + str(itenerario_marcado))
    print("Itinerario Onibus  : " + str(bus_id))
    print("Itinerario Tempo   : " + str(itenerario_tempo))
    print("Itinerario Valor   : " + str(itinerario_valor))

    

def solucao_parte_extra(entradas):
    pass


def espacar(s,tamanho):
    while len(s)<tamanho:
        s=s+" "
    
    return s

main()