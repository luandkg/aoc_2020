
from random import shuffle

def main():

    ADVENT_PROJETO = "2020"
    ADVENT_OF_CODE = "09"
    DATA_DA_RESOLUCAO = "2024 08 17"


    print("")
    print("---------- Advent of Code " + ADVENT_OF_CODE + " --------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : "+DATA_DA_RESOLUCAO)
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """"""
    entrada_texto  = criar_entradas()
    entrada_texto +="100\n"
    solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    solucao(transformar_texto_em_entradas(obter_entradas("inputs/input_" + ADVENT_OF_CODE + ".txt")))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")

    entrada_texto =""""""

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

    sequencia = 1
    VALIDAR_EM = 25

    anteriores = []

    tudo_ok = True
    xmas_corrompido_primeiro = 0;
    xmas_corrompido_primeiro_entrado = False

    for entrada in entradas:
        valido = False
        if sequencia > VALIDAR_EM:
            valido= False

            valor_somado = int(entrada)

            for arg1 in anteriores:
                for arg2 in anteriores:
                    if ( arg1 == arg2 ) == False :
                        if valor_somado == (arg1 + arg2) :
                            valido = True
                    if valido:
                        break
                if valido:
                    break
        

        
            if valido :
                print( espacar(sequencia,5) + " ::    "+ espacar(entrada,5))
            else:
                print( espacar(sequencia,5) + " ::    "+ espacar(entrada,5) + " -->> PROBLEMA")
                tudo_ok=False
                if xmas_corrompido_primeiro_entrado == False:
                    xmas_corrompido_primeiro_entrado=True
                    xmas_corrompido_primeiro = int(entrada)


        anteriores.append(int(entrada))
        sequencia+=1


    print("")
    if tudo_ok:
        print("Resultado : XMAS OK")
    else:
        print("Resultado : XMAS CORROMPIDO !!!")
        print("Primeiro Corrompido : " + str(xmas_corrompido_primeiro))




def solucao_parte_extra(entradas):

    sequencia = 1
    VALIDAR_EM = 25

    anteriores = []

    tudo_ok = True
    xmas_corrompido_primeiro = 0
    xmas_corrompido_primeiro_entrado = False

    for entrada in entradas:

        if xmas_corrompido_primeiro_entrado:
            break

        valido = False
        if sequencia > VALIDAR_EM:
            valido= False

            valor_somado = int(entrada)

            for arg1 in anteriores:
                for arg2 in anteriores:
                    if ( arg1 == arg2 ) == False :
                        if valor_somado == (arg1 + arg2) :
                            valido = True
                    if valido:
                        break
                if valido:
                    break
        

        
            if valido :
                print( espacar(sequencia,5) + " ::    "+ espacar(entrada,5))
            else:
                print( espacar(sequencia,5) + " ::    "+ espacar(entrada,5) + " -->> PROBLEMA")
                tudo_ok=False
                if xmas_corrompido_primeiro_entrado == False:
                    xmas_corrompido_primeiro_entrado=True
                    xmas_corrompido_primeiro = int(entrada)


        anteriores.append(int(entrada))
        sequencia+=1


    print("")
    if tudo_ok:
        print("Resultado : XMAS OK")
    else:
        print("Resultado : XMAS CORROMPIDO !!!")
        print("Primeiro Corrompido : " + str(xmas_corrompido_primeiro))

    xmas_corrompido_espacado = False
    xmas_problema_iniciar_em = 0
    xmas_problema_conjunto_encontrado = []


    while xmas_corrompido_espacado==False:

        print("Procurando iniciando em " + str(xmas_problema_iniciar_em))
        seq = 0
        xmas_problema_conjunto = []

        for entrada in entradas:
            i_entrada = int(entrada)

            if seq>=xmas_problema_iniciar_em:
                xmas_problema_conjunto.append(i_entrada)
                xmas_problema_conjunto_somatorio = somar_lista(xmas_problema_conjunto)

                #print("\t ++ " + str(i_entrada) + " :: " + str(xmas_problema_conjunto_somatorio))
                if xmas_problema_conjunto_somatorio == xmas_corrompido_primeiro:
                    xmas_corrompido_espacado=True
                    xmas_problema_conjunto_encontrado=xmas_problema_conjunto
                    break
                elif xmas_problema_conjunto_somatorio > xmas_corrompido_primeiro:
                    break

            seq+=1


        xmas_problema_iniciar_em+=1
        if(xmas_problema_iniciar_em>len(entradas)):
            break

    
    print("Espaco Problema Entrado : " + str(xmas_corrompido_espacado))

    if xmas_corrompido_espacado:

        xmas_corrompido_espacado_menor = xmas_problema_conjunto_encontrado[0]
        xmas_corrompido_espacado_maior = xmas_problema_conjunto_encontrado[0]

        for entrada in xmas_problema_conjunto_encontrado:
            print("\t - Espaco :: " + str(entrada))
            if (entrada < xmas_corrompido_espacado_menor):
                xmas_corrompido_espacado_menor=entrada
            
            if (entrada > xmas_corrompido_espacado_maior):
                xmas_corrompido_espacado_maior=entrada

        print("\t - Espaco Menor :: " + str(xmas_corrompido_espacado_menor))
        print("\t - Espaco Maior :: " + str(xmas_corrompido_espacado_maior))

        print("\t - Espaco Somatorio :: " + str(xmas_corrompido_espacado_menor+xmas_corrompido_espacado_maior))


def somar_lista(numeros):
    somatorio = 0
    for numero in numeros:
        somatorio+=numero
    return somatorio


def espacar(entrada,tamanho):

    s_entrada = str(entrada)

    while len(s_entrada)<tamanho:
        s_entrada += " "

    return s_entrada

def criar_entradas():
    texto = ""

    numero = 1
    numeros = []
    while numero<= 25:
        numeros.append(numero)
        numero+=1

    shuffle(numeros)

    for numerando in numeros:
        texto +=str(numerando) + "\n"

    
    return texto

main()