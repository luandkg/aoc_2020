def main():

    print("")
    print("---------- Advent of Code 08 --------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : 2024 08 16")
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """"""
    #solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    #solucao(transformar_texto_em_entradas(obter_entradas("inputs/input_08.txt")))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")

    entrada_texto =""""""

    #solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    #solucao_parte_extra(transformar_texto_em_entradas(obter_entradas("inputs/input_08.txt")))


def transformar_texto_em_entradas(entrada_texto):
    entradas = []
    for linha in entrada_texto.split("\n"):
        if(len(linha)>0):
            entradas.append(linha)
    return entradas;



main()