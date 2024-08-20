def main():

    ADVENTURE_PROJETO = "2020"
    ADVENTURE_OF_CODE = "11"
    DATA_DA_RESOLUCAO = "2024 08 20"


    print("")
    print("---------- Advent of Code " + ADVENTURE_OF_CODE + " --------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : "+DATA_DA_RESOLUCAO)
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    solucao(transformar_texto_em_entradas(obter_entradas("inputs/input_" + ADVENTURE_OF_CODE + ".txt")))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")

    entrada_texto =""".......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""
    solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    entrada_texto =""".##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##."""
    solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    entrada_texto ="""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
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

    colunas = 0
    linhas = 0

    for entrada in entradas:
        i_colunas =0
        for item in entrada:
            i_colunas+=1
        if i_colunas>colunas:
            colunas=i_colunas
        if len(entrada)>0:
            linhas+=1

    print("Linhas : "+str(linhas))
    print("Colunas : "+str(colunas))

    POSICAO_DESCONHECIDA = "0"

    POSICAO_CHAO = "."
    POSICAO_OCUPADA = "#"
    POSICAO_DISPONIVEL = "L"

    posicoes_anterior = [[0 for _ in range(colunas)] for _ in range(linhas)]
    posicoes = [[0 for _ in range(colunas)] for _ in range(linhas)]

    exibir_grade(posicoes)

    linha_corrente =0

    for entrada in entradas:

        coluna_corrente=0
        for posicao in entrada:

            posicao_tipo = POSICAO_DESCONHECIDA

            if posicao == "L":
                posicao_tipo=POSICAO_DISPONIVEL
            elif posicao == "#":
                posicao_tipo = POSICAO_OCUPADA
            elif posicao == ".":
                posicao_tipo = POSICAO_CHAO

            posicoes[linha_corrente][coluna_corrente] = posicao_tipo

            coluna_corrente+=1

        linha_corrente+=1

    copiar_grade(posicoes,posicoes_anterior)
    exibir_grade(posicoes)

    executando = True
    execucoes = 0

    igual=0
    execucao_estabilizada = 0
    execucao_final =0

    anterior_ocupadas = 0
    agora_ocupadas = 0

    while executando:
        execucoes+=1

        anterior_ocupadas = contagem_ocupados(posicoes_anterior)

        aplicar_regras(posicoes_anterior,posicoes,linhas,colunas)
        copiar_grade(posicoes,posicoes_anterior)
        aplicar_regras(posicoes_anterior,posicoes,linhas,colunas)
        exibir_grade(posicoes)

        agora_ocupadas = contagem_ocupados(posicoes)
        
        print("Oc - anterior = " + str(anterior_ocupadas))
        print("Oc - agora    = " + str(agora_ocupadas))

        if anterior_ocupadas == agora_ocupadas:
            if(igual==0):
                execucao_estabilizada=execucoes
            igual+=1
        else:
            igual=0

        if igual>=10:
            executando=False
            execucao_final = execucoes


    exibir_grade(posicoes)

    print()
    print("Execução Estabilizada = " + str(execucao_estabilizada))
    print("Execução Final        = " + str(execucao_final))

    print("Ocupados              = " + str(contagem_ocupados(posicoes)))


def solucao_parte_extra(entradas):

    colunas = 0
    linhas = 0

    for entrada in entradas:
        i_colunas =0
        for item in entrada:
            i_colunas+=1
        if i_colunas>colunas:
            colunas=i_colunas
        if len(entrada)>0:
            linhas+=1

    print("Linhas : "+str(linhas))
    print("Colunas : "+str(colunas))

    POSICAO_DESCONHECIDA = "0"

    POSICAO_CHAO = "."
    POSICAO_OCUPADA = "#"
    POSICAO_DISPONIVEL = "L"

    posicoes_anterior = [[0 for _ in range(colunas)] for _ in range(linhas)]
    posicoes = [[0 for _ in range(colunas)] for _ in range(linhas)]

    exibir_grade(posicoes)

    linha_corrente =0

    for entrada in entradas:

        coluna_corrente=0
        for posicao in entrada:

            posicao_tipo = POSICAO_DESCONHECIDA

            if posicao == "L":
                posicao_tipo=POSICAO_DISPONIVEL
            elif posicao == "#":
                posicao_tipo = POSICAO_OCUPADA
            elif posicao == ".":
                posicao_tipo = POSICAO_CHAO

            posicoes[linha_corrente][coluna_corrente] = posicao_tipo

            coluna_corrente+=1

        linha_corrente+=1

    copiar_grade(posicoes,posicoes_anterior)
    exibir_grade(posicoes)

    executando = True
    execucoes = 0

    igual=0
    execucao_estabilizada = 0
    execucao_final =0

    anterior_ocupadas = 0
    agora_ocupadas = 0

    while executando:
        execucoes+=1

        anterior_ocupadas = contagem_ocupados(posicoes_anterior)

        print("--->> Executar :")
        aplicar_regras_extra(posicoes_anterior,posicoes,linhas,colunas)
        copiar_grade(posicoes,posicoes_anterior)
        aplicar_regras_extra(posicoes_anterior,posicoes,linhas,colunas)
        exibir_grade(posicoes)

        agora_ocupadas = contagem_ocupados(posicoes)
        
        print("Oc - anterior = " + str(anterior_ocupadas))
        print("Oc - agora    = " + str(agora_ocupadas))

        if anterior_ocupadas == agora_ocupadas:
            if(igual==0):
                execucao_estabilizada=execucoes
            igual+=1
        else:
            igual=0

        if igual>=10:
            executando=False
            execucao_final = execucoes


    exibir_grade(posicoes)

    print()
    print("Execução Estabilizada = " + str(execucao_estabilizada))
    print("Execução Final        = " + str(execucao_final))

    print("Ocupados              = " + str(contagem_ocupados(posicoes)))


def exibir_grade(grade):

    print()
    print("--------- GRADE -----------")
    print()
    for indice,linha in enumerate(grade):
        print(str(indice) + " :: " + str(linha))

def contagem_ocupados(grade):

    ocupados = 0

    for linha in grade:
        for coluna in linha:
            if coluna == "#":
                ocupados+=1
    return ocupados

def copiar_grade(corrente,nova):

    for i_linha,linha in enumerate(corrente):
        for i_coluna,coluna in enumerate(linha):
            nova[i_linha][i_coluna] = coluna

def aplicar_regras(posicoes_anterior,posicoes,linhas,colunas):
       
    for i_linha,linha in enumerate(posicoes_anterior):
        for i_coluna,coluna in enumerate(linha):
            if coluna == "L":
                ocupados = contar_ao_redor("#",posicoes_anterior,linhas,colunas,i_linha,i_coluna)

                if ocupados ==0:
                    posicoes[i_linha][i_coluna] = "#"
            
            if coluna == "#":
                ocupados = contar_ao_redor("#",posicoes_anterior,linhas,colunas,i_linha,i_coluna)
                if ocupados >=4:
                    posicoes[i_linha][i_coluna] = "L"

def aplicar_regras_extra(posicoes_anterior,posicoes,linhas,colunas):
       
    for i_linha,linha in enumerate(posicoes_anterior):
        for i_coluna,coluna in enumerate(linha):
            if coluna == "L":
                ocupados = contar_ao_redor_extra("#",posicoes_anterior,linhas,colunas,i_linha,i_coluna)

                if ocupados ==0:
                    posicoes[i_linha][i_coluna] = "#"
            
            if coluna == "#":
                ocupados = contar_ao_redor_extra("#",posicoes_anterior,linhas,colunas,i_linha,i_coluna)
                if ocupados >=5:
                    posicoes[i_linha][i_coluna] = "L"


def contar_ao_redor(procurar_tipo,posicoes_anterior,linhas,colunas,i_linha,i_coluna):

    ocupados = 0

    movimentadores = [[-1,0],[+1,0],[0,-1],[0,+1], [-1,-1], [-1,+1],[+1,-1],[+1,+1]]

    for movimentador in movimentadores:

        o_linha = i_linha + movimentador[0]
        o_coluna = i_coluna + movimentador[1]

        if is_posicao_valida(o_linha,o_coluna,linhas,colunas):
            if posicoes_anterior[o_linha][o_coluna] == procurar_tipo:
                ocupados+=1
    
    return ocupados

def is_posicao_valida(i_linha,i_coluna,linhas,colunas):
    if i_linha>=0 and i_linha<linhas:
        if i_coluna>=0 and i_coluna<colunas:
            return True
    return False

def contar_ao_redor_extra(procurar_tipo,posicoes_anterior,linhas,colunas,i_linha,i_coluna):

    ocupados = 0

    movimentadores = [[-1,0],[+1,0],[0,-1],[0,+1], [-1,-1], [-1,+1],[+1,-1],[+1,+1]]

    for movimentador in movimentadores:

        o_linha = i_linha + movimentador[0]
        o_coluna = i_coluna + movimentador[1]

        if is_posicao_valida(o_linha,o_coluna,linhas,colunas):
            if posicoes_anterior[o_linha][o_coluna] == procurar_tipo:
                ocupados+=1
            elif posicoes_anterior[o_linha][o_coluna] == ".":
                if esta_ocupada_a_frente(procurar_tipo,posicoes_anterior,o_linha,o_coluna,linhas,colunas,movimentador):
                    ocupados+=1

    return ocupados

def esta_ocupada_a_frente(procurar_tipo,posicoes_anterior,o_linha,o_coluna,linhas,colunas,movimentador):

    o_linha=o_linha+movimentador[0]
    o_coluna=o_coluna + movimentador[1]

    if is_posicao_valida(o_linha,o_coluna,linhas,colunas):
        if posicoes_anterior[o_linha][o_coluna] == procurar_tipo:
            return True
        elif posicoes_anterior[o_linha][o_coluna] == ".":
            return esta_ocupada_a_frente(procurar_tipo,posicoes_anterior,o_linha,o_coluna,linhas,colunas,movimentador)
    else:
        return False





main()