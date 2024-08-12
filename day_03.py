def main():

    print("")
    print("---------- Advent of Code 03 --------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : 2024 08 08")
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->"""
    solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    solucao(obter_entradas("inputs/input_03.txt"))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")
    solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    solucao_parte_extra(obter_entradas("inputs/input_03.txt"))


def solucao(linhas):

    TIPO_NEVE = "."
    TIPO_ARVORE = "#"

    pos_x = 0
    arvores=0

    novas_linhas=[]    


    for linha in linhas:
        linha_pos_x =0
        linha_corrente=""

        for item in linha:
            if(pos_x == linha_pos_x):
                #print("@", end="")

                if item == TIPO_NEVE:
                    linha_corrente+="0"
                elif item == TIPO_ARVORE:
                    linha_corrente+="X"
                    arvores+=1

            else:
                #print(item, end="")
                linha_corrente+=item
            linha_pos_x+=1

        pos_x+=3
        if(pos_x>=len(linha)):
            pos_x=pos_x-(len(linha))
          
        novas_linhas.append(linha_corrente)
        
        #print()

    for linha in novas_linhas:
        print(linha)

   

    print()
    print("Árvores = " + str(arvores))


def solucao_parte_extra(linhas):

    d_1_1 = arvore_contagem(linhas,1,1)
    d_3_1 = arvore_contagem(linhas,3,1)
    d_5_1 = arvore_contagem(linhas,5,1)
    d_7_1 = arvore_contagem(linhas,7,1)
    d_1_2 = arvore_contagem(linhas,1,2)

    print()
    print("Árvores 1 x 1 = " + str(d_1_1))
    print("Árvores 3 x 1 = " + str(d_3_1))
    print("Árvores 5 x 1 = " + str(d_5_1))
    print("Árvores 7 x 1 = " + str(d_7_1))
    print("Árvores 1 x 2 = " + str(d_1_2))

    print("Resultado = " + str(d_1_1 * d_3_1 * d_5_1 * d_7_1 * d_1_2))

   



def arvore_contagem(linhas, DELTA_X, DELTA_Y):
    TIPO_NEVE = "."
    TIPO_ARVORE = "#"

    pos_x = 0
    pos_y = 0


    arvores=0

    novas_linhas=[]    

    linha_contando =0

    for linha in linhas:
        linha_pos_x =0
        linha_corrente=""

        if pos_y == linha_contando:
            for item in linha:
                if(pos_x == linha_pos_x):
                    #print("@", end="")

                    if item == TIPO_NEVE:
                        linha_corrente+="0"
                    elif item == TIPO_ARVORE:
                        linha_corrente+="X"
                        arvores+=1

                else:
                    #print(item, end="")
                    linha_corrente+=item
                linha_pos_x+=1
            pos_y+=DELTA_Y
            pos_x+=DELTA_X
        

        if(pos_x>=len(linha)):
            pos_x=pos_x-(len(linha))

        linha_contando+=1
        print("Linha Contagem :: "+str(linha_contando) + " :: "+ str(pos_y))
          
        novas_linhas.append(linha_corrente)
        
        #print()

    for linha in novas_linhas:
        print(linha)

   

    print()
    print("Árvores = " + str(arvores))
    return arvores





def transformar_texto_em_entradas(entrada_texto):
    entradas = []
    for linha in entrada_texto.split("\n"):
        entradas.append(linha)
    return entradas;

def obter_entradas(arquivo_caminho):
    dados = []

    arquivo = open(arquivo_caminho)
    for linha in arquivo.readlines():
        for linha_sub in linha.split("\n"):
            if(len(linha_sub)>0):
                dados.append(linha_sub)

    return dados

main()