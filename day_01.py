

def main():

    print("")
    print("---------- Advent of Code 01 --------------")
    print("")

    print(" + INTRODUÇÃO")
    print("")
    solucao([1721,979,366,299,675,1456])


    print("")
    print(" + PROBLEMA")
    print("")
    solucao(obter_entradas("inputs/input_01.txt"))


    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    solucao_parte_extra(obter_entradas("inputs/input_01.txt"))



def obter_entradas(arquivo_caminho):
    dados = []

    arquivo = open(arquivo_caminho)
    for linha in arquivo.readlines():
        dados.append(int(linha))

    return dados



def solucao(entradas):
    deve_ser_igual = 2020

    for entrada_1 in entradas:
        
    ## print("Entrada 1 "+ str(entrada_1))
        for entrada_2 in entradas:
            ##print("\t Entrada 2 "+str(entrada_2))
            valor_somatorio = entrada_1 + entrada_2
            ##print("\t Valor : "+str(valor_local))
            ##print("\t Igual : "+str(entrada_1) + " e "+ str(entrada_2) + " = " + str(valor_somatorio))

            if valor_somatorio == deve_ser_igual :
                valor_produto = entrada_1*entrada_2
                print("\t -->> "+str(entrada_1) + " e "+ str(entrada_2) + " = " + str(valor_produto))

def solucao_parte_extra(entradas):
    deve_ser_igual = 2020

    for entrada_1 in entradas:
        ## print("Entrada 1 "+ str(entrada_1))
        for entrada_2 in entradas:
            ##print("\t Entrada 2 "+str(entrada_2))
            for entrada_3 in entradas:
                valor_somatorio = entrada_1 + entrada_2+entrada_3
                ##print("\t Valor : "+str(valor_local))
                ##print("\t Igual : "+str(entrada_1) + " e "+ str(entrada_2) + " = " + str(valor_somatorio))

                if valor_somatorio == deve_ser_igual :
                    valor_produto = entrada_1*entrada_2*entrada_3
                    print("\t -->> "+str(entrada_1) + " e "+ str(entrada_2) + " e "+ str(entrada_3)+" = " + str(valor_produto))


main()