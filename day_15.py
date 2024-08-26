def main():

    ADVENT_PROJETO = "2020"
    ADVENT_OF_CODE = "15"
    DATA_DA_RESOLUCAO = "2024 08 24"


    print("")
    print("---------- Advent of Code " + ADVENT_OF_CODE + " --------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : "+DATA_DA_RESOLUCAO)
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """0,3,6"""
    solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    entrada_texto = """2,0,1,9,5,19"""
    solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")

    entrada_texto ="""3,2,1"""
    solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    entrada_texto = """2,0,1,9,5,19"""
    solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))


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

    rodada = 1
    rodada_parar = 2020

    valores = []
    for entrada in entradas[0].split(","):
        valores.append(int(entrada))

    numero_corrente = 0

    ate = len(valores)

    while rodada<=rodada_parar:

        if rodada == 1:
            numero_corrente = 0
        
        numero_atual = 0
        if rodada -1 < ate:
            numero_atual = valores[rodada-1]
        else:

            existe = 0
            primeira_vez = 0
            ultima_vez = 0

            sequencial = 1
            for num in valores:
                if num == numero_corrente:
                    if existe == 0:
                        primeira_vez = sequencial
                        ultima_vez = sequencial
                    else:
                        primeira_vez = ultima_vez
                        ultima_vez = sequencial
                    existe+=1

                sequencial +=1



            #for num in valores:
            #    print("\t\t V = " + str(num))

            #print("Numero : " + str(numero_corrente))
            #print("Existe : " + str(existe))

            if existe == 1:
                numero_atual = 0
            else:
                #print("Primeira : " + str(primeira_vez))
                #print("Ultima   : " + str(ultima_vez))
                numero_atual = ultima_vez - primeira_vez



        
        print(" - Rodada " + str(rodada) + " : " + "O " + str(rodada) + "º número dito é : " + str(numero_atual))
        rodada+=1
        numero_corrente = numero_atual
        if rodada -1 > ate:
            valores.append(numero_corrente)

from collections import defaultdict, deque

def solucao_parte_extra(entradas):

    rodada_parar = 30000000
    #rodada_parar = 2020

    from collections import defaultdict, deque

    valores = []
    for entrada in entradas[0].split(","):
        valores.append(int(entrada))

    exibir =0
    valores_indexados, ultimo = defaultdict(lambda: deque([],maxlen=2)), valores[-1]
    for i in range(1,len(valores)+1): valores_indexados[valores[i-1]].append(i)
    for i in range(i+1,rodada_parar+1):
        if len(valores_indexados[ultimo])<2: ultimo = 0
        else: ultimo = valores_indexados[ultimo][-1]-valores_indexados[ultimo][-2]
        valores_indexados[ultimo].append(i)

        exibir +=1
        if exibir == 1000:
            exibir = 0
            print("\t ++ Valor indexado " + str(ultimo) + " = " + str(i))

    print("Valor " + str(rodada_parar) + " = " +str(ultimo))
        




main()