def main():

    ADVENT_PROJETO = "2020"
    ADVENT_OF_CODE = "14"
    DATA_DA_RESOLUCAO = "2024 08 23"
    STATUS = "FALHEI"


    print("")
    print("---------- Advent of Code " + ADVENT_OF_CODE + " --------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : "+DATA_DA_RESOLUCAO)
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    solucao(transformar_texto_em_entradas(obter_entradas("inputs/input_" + ADVENT_OF_CODE + ".txt")))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")

    entrada_texto =""""""

    #solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    #solucao_parte_extra(transformar_texto_em_entradas(obter_entradas("inputs/input_" + ADVENT_OF_CODE + ".txt")))


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

class Memoria:

    def __init__(self,mascara):
        self.mascara = mascara
        self.valores = []

    def adicionar(self,posicao,valor):
        self.valores.append(Registro(posicao,valor))

    def getMascara(self):
        return self.mascara
    
    def getValores(self):
        return self.valores
    

class Registro:
    def __init__(self,posicao,valor):
        self.posicao = posicao
        self.valor=valor
    
    def getPosicao(self):
        return self.posicao
    
    def getValor(self):
        return self.valor

def solucao(entradas):
    
    memorias = []

    memoria_corrente = None


    for entrada in entradas:
        #print(entrada)

        if entrada.startswith("mask"):
            memoria_corrente = Memoria(entrada.replace("mask = ",""))
            memorias.append(memoria_corrente)
        elif entrada.startswith("mem"):

            partes = entrada.split(" ")

            parte_zero = partes[0].replace("mem[","").replace("]","")
            parte_dois = partes[2]

            memoria_corrente.adicionar(int(parte_zero),int(parte_dois))

    
    for memoria in memorias:
        print("++ Memoria : " + memoria.getMascara())

        somatorio_geral = 0

        print()
        for item in memoria.getValores():
            print("\t    - " + str(item.getPosicao()) + " :: " + str(item.getValor()))

        print()

        memoria_inicializada = binario(0)

        print()
        print("\t -->> Memoria     : " + memoria_inicializada)
        print()

        somatorio = 0

        for item in memoria.getValores():

            item_valor_binario =     binario(item.getValor())
            item_mascara = memoria.getMascara()
            item_resultado = aplicar(item_valor_binario,item_mascara)

            valor_retorno = obter_valor(item_resultado)

            memoria_inicializada= aplicar_posicao(memoria_inicializada,item.getPosicao(),item_resultado)

            mem_retorno = obter_valor(memoria_inicializada)

            print("\t -->> Valor       : " + item_valor_binario + " (decimal " + str(item.getValor()) + ")")
            print("\t -->> Mascara     : " + item_mascara)
            print("\t -->> Resultado   : " + item_resultado + " (decimal " + str(valor_retorno) + ")")
            print()
            print("\t -->> Memoria     : " + memoria_inicializada + " (decimal " + str(mem_retorno) + ")")
            print()

            somatorio+=valor_retorno

    
        print("Somatorio = " + str(somatorio))
        somatorio_geral+=somatorio

    print("Somatorio Geral = " + str(somatorio_geral))



    

def binario(valor):

    sequencia = ""
    while valor>1:
        quociente = valor // 2
        resto = valor % 2
        valor = quociente

        sequencia =str(resto) + sequencia

    sequencia =str(valor) + sequencia


    while len(sequencia)<36:
        sequencia = "0" + sequencia

    return str(sequencia)

def aplicar(item_valor_binario,item_mascara):
    item_resultado = ""

    if (len(item_valor_binario) == len(item_mascara)):
        indice = 0
        while indice < len(item_valor_binario):
            
            m = item_mascara[indice]
            v = item_valor_binario[indice]

            r = ""

            if m == "X":
                r=v
            else:
                if m == "0":
                    r = "0"
                elif m == "1":
                    r= "1"

            item_resultado+=r
            indice+=1

    
    return item_resultado

def obter_valor(entrada):

    tamanho = len(entrada)
    indice = 0
    while indice<tamanho:
        c = entrada[indice]
        if (c == "1"):
            break
        indice+=1

    valor = 0
    base = 1
    exp = tamanho-indice-1
    while indice<tamanho:
        aqui = int(entrada[indice])
        base = pow(2,exp)
        valor += aqui * base

        #print("Indo " + str(entrada[indice]) + " Base = " + str(base) + " Valor = " + str(valor))
        indice+=1
        exp-=1


    return valor


def aplicar_posicao(memoria,posicao,novo_valor):


    validado = ""
    validou = False
    for item in novo_valor:
        if not validou  and item == "1":
            validou = True
        
        if validou :
            validado+=item

    #print("Valor    : " + str(novo_valor))
    #print("Validado : " + str(validado))
    #print("Posicao  : " + str(posicao))

    posicao_real = len(memoria) - posicao
    #print("Posicao  : " + str(posicao_real))

    nova_memoria = ""
    indice = 0
    indice_dois=0

    while indice<len(memoria):

        if indice <= posicao_real:
            nova_memoria=nova_memoria + memoria[indice]
        else:
            if indice_dois < len(validado):
                nova_memoria=nova_memoria + validado[indice_dois]
            else:
                nova_memoria=nova_memoria + memoria[indice]

            indice_dois+=1

        #print("M :: " + nova_memoria)
        indice+=1



    return nova_memoria

def solucao_parte_extra(entradas):
    pass


main()