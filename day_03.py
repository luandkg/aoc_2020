def main():

    print("")
    print("---------- Advent of Code 03 --------------")
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
    #solucao(obter_entradas("inputs/input_03.txt"))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")
    #solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    #solucao_parte_extra(obter_entradas("inputs/input_03.txt"))


def solucao(linhas):

    pos_x = 0
    arvores=0

    novas_linhas=[]    


    for linha in linhas:
        linha_pos_x =0
        linha_corrente=""
        for item in linha:
            if(pos_x == linha_pos_x):
                #print("@", end="")

                if item == ".":
                    linha_corrente+="0"
                elif item == "#":
                    linha_corrente+="X"
                    arvores+=1

            else:
                #print(item, end="")
                linha_corrente+=item
            linha_pos_x+=1
        novas_linhas.append(linha_corrente)
        pos_x+=3
        #print()

    
    for linha in novas_linhas:
        print(linha)

    print()
    print("Árvores = " + str(arvores))


def transformar_texto_em_entradas(entrada_texto):
    entradas = []
    for linha in entrada_texto.split("\n"):
        entradas.append(linha)
    return entradas;


main()