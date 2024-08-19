def main():

    ADVENTURE_PROJETO = "2020"
    ADVENTURE_OF_CODE = "10"
    DATA_DA_RESOLUCAO = "2024 08 19"


    print("")
    print("---------- Advent of Code " + ADVENTURE_OF_CODE + " --------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : "+DATA_DA_RESOLUCAO)
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """16
10
15
5
1
11
7
19
6
12
4"""
    solucao(transformar_texto_em_entradas(entrada_texto))

    entrada_texto = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
    solucao(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA")
    print("")
    solucao(transformar_texto_em_entradas(obter_entradas("inputs/input_" + ADVENTURE_OF_CODE + ".txt")))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")

    entrada_texto =""""""

    #solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    #solucao_parte_extra(transformar_texto_em_entradas(obter_entradas("inputs/input_" + ADVENTURE_OF_CODE + ".txt")))


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

    maior = 0
    corrente_anterior = 0

    correntes = []

    for entrada in entradas:
        corrente = int(entrada)
        correntes.append(corrente)
        if corrente > maior:
            maior= corrente

    maior = maior +3
    correntes.append(maior)

    correntes.sort()

    contagem_um = 0
    contagem_tres = 0

    for corrente in correntes:
        print("Corrente : " + str(corrente))
       
        diferenca = corrente - corrente_anterior
        print("\t + Diff : " + str(diferenca))
        if diferenca == 1:
            contagem_um +=1
        elif diferenca==3:
            contagem_tres+=1
        
        corrente_anterior = corrente

    
    print("")
    print(" - Maior Corrente = " + str(maior))
    print(" - Diff 1 = " + str(contagem_um))
    print(" - Diff 3 = " + str(contagem_tres))
    print("")
    print(" - Multiplicado = " + str(contagem_um*contagem_tres))



def solucao_parte_extra(entradas):
    pass


main()