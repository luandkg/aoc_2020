def main():

    ADVENT_PROJETO = "2020"
    ADVENT_OF_CODE = "16"
    DATA_DA_RESOLUCAO = "2024 08 26"


    print("")
    print("---------- Advent of Code " + ADVENT_OF_CODE + " --------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : "+DATA_DA_RESOLUCAO)
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
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

    validos = []
    meu_ticket = []
    tickets_proximos = []

    ESTADO_OBTENDO_VALIDOS  = 0
    ESTADO_MEU_TICKET       = 1
    ESTADO_TICKETS_PROXIMOS = 2

    ESTADO_CORRENTE = ESTADO_OBTENDO_VALIDOS

    for linha in entradas:

        if ESTADO_CORRENTE == ESTADO_TICKETS_PROXIMOS:
            for ticket in linha.split(","):
                    tickets_proximos.append(int(ticket))

        if ESTADO_CORRENTE == ESTADO_MEU_TICKET:
            if linha == "nearby tickets:":
                ESTADO_CORRENTE=ESTADO_TICKETS_PROXIMOS
            else:
                for ticket in linha.split(","):
                    meu_ticket.append(int(ticket))


        if ESTADO_CORRENTE == ESTADO_OBTENDO_VALIDOS:
            if linha == "your ticket:":
                ESTADO_CORRENTE=ESTADO_MEU_TICKET
            else:
                ticket_valido_nome = linha.split(":")[0]
                ticket_valido_intervalo = linha.split(":")[1].strip()
                print("\t ++ TICKET VALIDO :: " + ticket_valido_nome + " = " + ticket_valido_intervalo)
                for intervalo in ticket_valido_intervalo.split("or"):
                    intervalo = intervalo.strip()
                    intervalo_inicio = int(intervalo.split("-")[0])
                    intervalo_fim = int(intervalo.split("-")[1])

                    print("\t\t -- " + str(intervalo_inicio) + " ate " + str(intervalo_fim))
                    #print("++ " + str(list(range(intervalo_inicio,intervalo_fim+1))))

                    for ticket_valido in list(range(intervalo_inicio,intervalo_fim+1)):
                        validos.append(ticket_valido)


    print("\t MEU TICKET       : " + str(meu_ticket))
    print("\t TICKETS PROXIMOS : " + str(tickets_proximos))

    ticket_scanning_error_rate = 0

    for ticket in tickets_proximos:
        if not ticket in validos:
            ticket_scanning_error_rate+=ticket

    print()
    print(">> Ticket Scanning Error Rate : " + str(ticket_scanning_error_rate))





def solucao_parte_extra(entradas):
    pass


main()