def main():

    print("")
    print("---------- Advent of Code 07 --------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : 2024 08 14")
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
    #solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    #solucao(transformar_texto_em_entradas(obter_entradas("inputs/input_07.txt")))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")

    entrada_texto ="""shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

    solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    #solucao_parte_extra(transformar_texto_em_entradas(obter_entradas("inputs/input_07.txt")))


def transformar_texto_em_entradas(entrada_texto):
    entradas = []
    for linha in entrada_texto.split("\n"):
        if(len(linha)>0):
            entradas.append(linha)
    return entradas;

def dividir_em_partes(entrada):
    return entrada.split(" ")

def obter_entradas(arquivo_caminho):
    
    texto = ""

    arquivo = open(arquivo_caminho)
    for linha in arquivo.readlines():
        texto = texto + linha

    return texto

class Bagagem:

    def __init__(self):
        self.nome = ""
        self.vazia=True
        self.shiny_gold = False
        self.shinigado = False
        self.por= ""
        self.interno = []
    
    def setNome(self,nome):
        self.nome=nome

    def getNome(self):
        return self.nome
    
    def adicionar(self,internamente):
        self.vazia=False
        self.interno.append(internamente)
    
    def getInterno(self):
        return self.interno

    def setVazia(self,valor):
        self.vazia=valor
    
    def isVazia(self):
        return self.vazia

    def isShinyGold(self):
        return self.shiny_gold
    
    def setShinyGold(self,valor):
        self.shiny_gold=valor

    def shinigado(self,valor):
        self.shinigado = valor

    def isShinigado(self):
        return self.shinigado
    
    def shinigar(self,por):
        self.shinigado=True
        self.por=por

    def getPor(self):
        return self.por
    

class BagagemInterna:
    
    def __init__(self):
        self.nome=""
        self.quantidade =0

    def setNome(self,nome):
        self.nome=nome
    def getNome(self):
        return self.nome
    
    def setQuantidade(self,quantidade):
        self.quantidade=quantidade
    def getQuantidade(self):
        return self.quantidade;

def solucao(entradas):

    bagagens = []

    for entrada in entradas:
        partes = dividir_em_partes(entrada)
    

        bagagem_corrente = Bagagem()
        bagagens.append(bagagem_corrente)

        bagagem_corrente.setNome(partes[0] + " "+ partes[1])

        resto = ""

        for i,palavra in enumerate(partes):
            if i>=2:
                #print(str(i) + " :: "+ palavra)
                resto+=" "+palavra
                if palavra == "bag," or palavra == "bags," or palavra == "bag." or palavra == "bags.":
                    bagagem_interna = partes[i-2] + " " + partes[i-1]
                    if(bagagem_interna == "no other"):
                        bagagem_corrente.setVazia(True)
                    else:
                        bagagem_corrente.adicionar(bagagem_interna)
                        if bagagem_interna == "shiny gold":
                            bagagem_corrente.setShinyGold(True)



        #print("\t ++ "+ bagagem_corrente.getNome() + " < " + resto + " >")

    for bagagem in bagagens:
        if(bagagem.isVazia()):
            print("\t -- "+bagagem.getNome() + " #VAZIA")
        else:
            print("\t -- "+bagagem.getNome())

        for interno in bagagem.getInterno():
            print("\t\t + "+interno)

    visualizar_geral(bagagens)
    shinigar_completamente(bagagens)
    visualizar_geral(bagagens)

    contagem_shiny_gold = 0
    for bagagem in bagagens:
        if bagagem.isShinyGold():
            contagem_shiny_gold+=1

    print()
    print("ShinyGold = "+str(contagem_shiny_gold))


def visualizar_geral(bagagens):
    print()
    print("----------- SHINY GOLD -------------")
    for bagagem in bagagens:

        if(bagagem.isShinyGold()):
            print("\t -- "+bagagem.getNome())

    print()
    print("----------- SHINIGADOS -------------")
    for bagagem in bagagens:

        if(bagagem.isShinigado()):
            print("\t -- "+bagagem.getNome() + " --->> "+ bagagem.getPor())

def shinigar_completamente(bagagens):
    
    todos=False

    while(todos == False):

        #visualizar_geral(bagagens)
        shinigar(bagagens)

        shinigado = 0
        for bagagem in bagagens:
            if bagagem.isShinigado():
                shinigado+=1
        if len(bagagens) == shinigado:
            todos=True


def shinigar(bagagens):
    
    print()
    print("----------- SHINIGAR -------------")

    for bagagem in bagagens:

        if not bagagem.isShinigado() and bagagem.isShinyGold():
            bagagem.shinigar("ShinyGold")
        if  not bagagem.isShinigado() and bagagem.isVazia():
            bagagem.shinigar("VAZIA")

        if not bagagem.isShinigado():
            if(not bagagem.isShinyGold() and not bagagem.isVazia()):
                print("\t -- "+bagagem.getNome() + " ->> Shinigando...")

                verificados = 0

                for interno in bagagem.getInterno():
                    #print("\t :: "+interno)

                    bagagem_localizada = False
                    
                    for procurando in bagagens:
                        if procurando.getNome() == interno:
                            bagagem_localizada=True
                            if procurando.isShinigado():
                                verificados+=1
                                if procurando.isShinyGold():
                                    bagagem.setShinyGold(True)
                                    bagagem.shinigar(interno)
                                    break
                            elif not procurando.isShinigado():
                                print("\t\t -- NAO SHINIGADO AINDA "+procurando.getNome())

                    if not bagagem_localizada:
                        print("\t\t -- DESCONHECIDA :: "+bagagem.getNome())

                if (len(bagagem.getInterno()) == verificados):
                    bagagem.shinigar("ZERADO")




def solucao_parte_extra(entradas):

    bagagens = []

    for entrada in entradas:
        partes = dividir_em_partes(entrada)
    

        bagagem_corrente = Bagagem()
        bagagens.append(bagagem_corrente)

        print("@"+entrada)
        bagagem_corrente.setNome(partes[0] + " "+ partes[1])

        resto = ""

        for i,palavra in enumerate(partes):
            if i>=2:
                #print(str(i) + " :: "+ palavra)
                resto+=" "+palavra
                if palavra == "bag," or palavra == "bags," or palavra == "bag." or palavra == "bags.":
                    bagagem_interna = partes[i-2] + " " + partes[i-1]
                    if(bagagem_interna == "no other"):
                        bagagem_corrente.setVazia(True)
                    else:
                        bagagem_corrente.adicionar(bagagem_interna)
                        if bagagem_interna == "shiny gold":
                            bagagem_corrente.setShinyGold(True)



        print("\t ++ "+ bagagem_corrente.getNome() + " < " + resto + " >")

    for bagagem in bagagens:
        if(bagagem.isVazia()):
            print("\t -- "+bagagem.getNome() + " #VAZIA")
        else:
            print("\t -- "+bagagem.getNome())

        for interno in bagagem.getInterno():
            print("\t\t + "+interno)

    visualizar_geral(bagagens)
    shinigar_completamente(bagagens)
    visualizar_geral(bagagens)

    contagem_shiny_gold = 0
    for bagagem in bagagens:
        if bagagem.isShinyGold():
            contagem_shiny_gold+=1

    print()
    print("ShinyGold = "+str(contagem_shiny_gold))




main()