def main():

    print("")
    print("---------- Advent of Code 06--------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : 2024 08 12")
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    solucao(transformar_texto_em_entradas(obter_entradas("inputs/input_06.txt")))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")
    #solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    #solucao_parte_extra(transformar_texto_em_entradas(obter_entradas("inputs/input_06.txt")))


def transformar_texto_em_entradas(entrada_texto):
    entradas = []
    for linha in entrada_texto.split("\n"):
        for parte in linha.split(" "):
            entradas.append(parte)
    return entradas;

def obter_entradas(arquivo_caminho):
    
    texto = ""

    arquivo = open(arquivo_caminho)
    for linha in arquivo.readlines():
        texto = texto + linha

    return texto

class Grupo:
    participantes=[]

    def __init__(self):
        self.participantes=[]
        
    def adicionar_participante(self,participante):
        self.participantes.append(participante)

    def get_participantes(self):
        return self.participantes

def solucao(entradas):

    grupos = []
    grupo_corrente = Grupo()

    for entrada in entradas:
        if entrada == "":
            grupos.append(grupo_corrente)
            grupo_corrente = Grupo()
            print("-----")

        else:
            grupo_corrente.adicionar_participante(entrada)
        print(entrada)

    if len(grupo_corrente.get_participantes())>0:
        grupos.append(grupo_corrente)

    respostas_somatorio = 0

    for grupo_id,grupo in enumerate(grupos):
        print("Grupo :: "+ str(grupo_id+1) + " :: com "+ str(len(grupo.get_participantes())))

        respostas_unicas = set()

        for respostas in grupo.get_participantes():
            print("\tParticipante : "+respostas)
            for resposta in respostas:
                respostas_unicas.add(resposta)

        #for resposta_item in respostas_unicas:
            #print("Unica : "+ resposta_item)

        print("Respostas : "+ str(len(respostas_unicas)))
        respostas_somatorio+=len(respostas_unicas)
    
    print("Respostas Somatorio : "+ str(respostas_somatorio))


main()