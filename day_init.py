def main():

    ADVENTURE_PROJETO = "2020"
    ADVENTURE_OF_CODE = "09"
    DATA_DA_RESOLUCAO = "2024 08 17"


    print("")
    print("---------- Advent of Code " + ADVENTURE_OF_CODE + " --------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : "+DATA_DA_RESOLUCAO)
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """"""
    #solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    #solucao(transformar_texto_em_entradas(obter_entradas("inputs/input_" + ADVENTURE_OF_CODE + ".txt")))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")

    entrada_texto =""""""

    solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    solucao_parte_extra(transformar_texto_em_entradas(obter_entradas("inputs/input_" + ADVENTURE_OF_CODE + ".txt")))


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
    pass

def solucao_parte_extra(entradas):
    pass


main()