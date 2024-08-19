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
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")

    entrada_texto ="""16
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

    solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

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
    correntes = []

    maior = 0

    for entrada in entradas:
        corrente = int(entrada)
        correntes.append(corrente)
        if corrente > maior:
            maior= corrente

    maior = maior +3
    #correntes.append(maior)

    maximo_sequenciador = len(correntes)

    correntes.sort()

    tomada  = 0
    carragemento = maior

    sequencias = []

    valor_aqui = 0

    for op in correntes:
        if op>valor_aqui:
            if (op - valor_aqui)<=3:

                print("\t - opcao :: " + str(op))

                sequencia = []
                sequencia.append(op)
                #interno(correntes,op,sequencia,sequencias,carragemento,maximo_sequenciador)

    
    primeiros = []
            
    for indice,sequencia in enumerate(sequencias):
        print("S - "+  str(indice+1) + " = (" + str(tomada) + ") -> ", end = " ")
        print("(" + str(sequencia) + ")", end = " ")
        print(" -> (" + str(carragemento) + ")", end = " ")

        print("")

        if not int(sequencia[0]) in primeiros:
            primeiros.append(int(sequencia[0]))

    print("")
    print("Conjunto = " + str(correntes))
    print("Tamanho = " + str(len(correntes)))

    correntes.sort()
    correntes = correntes + [max(correntes) + 3]

    respostas = {}
    respostas[0] = 1
    for corrente in correntes:
        respostas[corrente] = respostas.get(corrente - 1, 0) + respostas.get(corrente - 2, 0) + respostas.get(corrente - 3, 0)

    print("Combinacoes = " + str(respostas[correntes[-1]]))

    

def interno(correntes,valor_aqui,sequencia,sequencias,carregamento,maximo_sequenciador):

    opcoes = []

    for proximo in correntes:
        if proximo>valor_aqui:
            if (proximo - valor_aqui)<=3:
                opcoes.append(proximo)

            #print("Corrente : "+str(valor_aqui))
    
    for op in opcoes:
        print("\t - opcao :: " + str(op))

        nova_sequencia = []

        for item in sequencia :
            nova_sequencia.append(item)

        nova_sequencia.append(op)
        interno(correntes,op,nova_sequencia,sequencias,carregamento,maximo_sequenciador)
    

    if len(opcoes) == 0:
        ultimo = sequencia[len(sequencia)-1]
        if ultimo + 3 <=carregamento:
            adicionar_entao(sequencia,sequencias)
            print("Sequencia Geral :: " + str(len(sequencia)) + " de " + str(maximo_sequenciador))
            print("Sequencias -->> " + str(len(sequencias)))



def adicionar_entao(sequencia,sequencias):
    valido = True

    for seq in sequencias:

        i_seq = len(seq)
        o_seq = len(sequencia)
        validando = 0

        if i_seq == o_seq:
            index=0
            while index<i_seq:
                if sequencia[index] == seq[index]:
                    validando+=1
                index+=1
            
            if validando==i_seq:
                valido=False

    

    if valido:
        sequencias.append(sequencia)
    

def valor_da_lista(lista):
    valor= 0
    for v in lista:
        valor+=v

    return valor

def exibir(lista):

    for item in lista:
        print(str(item) , end=" ")


main()