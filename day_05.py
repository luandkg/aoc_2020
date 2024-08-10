def main():

    print("")
    print("---------- Advent of Code 05 --------------")
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """BBFFBBFRLL"""
    solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    solucao(transformar_texto_em_entradas(obter_entradas("inputs/input_05.txt")))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")
    #solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    #solucao_parte_extra(transformar_texto_em_entradas(obter_entradas("inputs/input_05.txt")))


def transformar_texto_em_entradas(entrada_texto):
    entradas = []
    for linha in entrada_texto.split("\n"):
        for parte in linha.split(" "):
            entradas.append(parte)
    return entradas;

def obter_entradas(arquivo_caminho):
    
    texto = ""

    arquivo = open(arquivo_caminho)
    for linha in arquivo.readlines():
        texto = texto + linha

    return texto

def obter_linhas_nao_vazias(linhas):
    linhas_nao_vazias = []
    for linha in linhas:
        if(len(linha)>0):
            linhas_nao_vazias.append(linha)
    return linhas_nao_vazias


def solucao(linhas):

    linhas_nao_vazias = obter_linhas_nao_vazias(linhas)
  
    seat_id_highest = 0
    
    for linha in linhas_nao_vazias:

        primeiro_7 = ""
        resto = ""

        for i,letra in enumerate(linha):
            if(i<7):
                primeiro_7+=letra
            else:
                resto+=letra

        

        print("\t + "+linha + " ->> "+ primeiro_7 + " :: "+ resto)

        print("\t----- PARTE A ------")

        parte_a = 0
        parte_b = 0

        minimo = 0
        maximo = 127
        intervalo = maximo-minimo
        intervalo_centro = int(intervalo/2)

        for letra in primeiro_7:
            metade = int(intervalo/2)
            modo = ""
            if letra=="F":
                modo="Lower Half"
                minimo=intervalo_centro-metade
                maximo=intervalo_centro
            elif letra=="B":
                modo="Upper Half"
                minimo=intervalo_centro+1
                maximo=(intervalo_centro+metade)+1

            intervalo = maximo - minimo
            intervalo_centro = int(intervalo/2)+minimo


            print("\t = "+letra + "  ::  "+ modo +" -->> "+ str(minimo) + " -- " + str(maximo))
            parte_a = min(minimo,maximo)

        print("\t----- PARTE B ------")
        minimo = 0
        maximo = 7
        intervalo = maximo-minimo
        intervalo_centro = int(intervalo/2)

        for letra in resto:
            metade = int(intervalo/2)
            modo = ""
            if letra=="L":
                modo="Lower Half"
                minimo=intervalo_centro-metade
                maximo=intervalo_centro
            elif letra=="R":
                modo="Upper Half"
                minimo=intervalo_centro+1
                maximo=(intervalo_centro+metade)+1

            intervalo = maximo - minimo
            intervalo_centro = int(intervalo/2)+minimo


            print("\t = "+letra + "  ::  "+ modo +" -->> "+ str(minimo) + " -- " + str(maximo))
            parte_b = min(minimo,maximo)



        seat_id = (parte_a *8)+parte_b
        print("\t++ Parte Alfa : "+ str(parte_a))
        print("\t++ Parte Beta : "+ str(parte_b))
        print("\t++ SeatID = "+str(seat_id))

        if(seat_id>seat_id_highest):
            seat_id_highest=seat_id

    
    print()
    print("++ Maior SeatID = "+str(seat_id_highest))




main()