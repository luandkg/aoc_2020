def main():

    print("")
    print("---------- Advent of Code 08 --------------")
    print("")
    print("EU : LUAN FREITAS - luandkg@gmail.com")
    print("DATA : 2024 08 16")
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    #solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    #solucao(transformar_texto_em_entradas(obter_entradas("inputs/input_08.txt")))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")

    entrada_texto ="""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

    solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    solucao_parte_extra(transformar_texto_em_entradas(obter_entradas("inputs/input_08.txt")))


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

class Opcode:
    def __init__(self,instrucao,argumento):
        self.instrucao = instrucao
        self.argumento = argumento
        self.executada = 0

    def getInstrucao(self):
        return self.instrucao
    
    def setInstrucao(self,instrucao):
        self.instrucao = instrucao

    def getArgumento(self):
        return self.argumento

    def __str__(self):
        return " " + espacar(self.instrucao,5) + " :: "+ espacar(str(self.argumento),5) + " | "
    
    def executar(self):
        self.executada+=1

    def getExecucoes(self):
        return self.executada


def espacar(entrada,tamanho):
    while len(entrada)<tamanho:
        entrada += " "

    return entrada


def solucao(entradas):

    instrucoes = []

    for instrucao in entradas:
        tx_instrucao = instrucao.split(" ")[0]
        tx_argumento = instrucao.split(" ")[1]

        instrucoes.append(Opcode(tx_instrucao,int(tx_argumento)))
       
    ip = 0
    acc = 0
    executando = True

    sequencia = 1


    while(executando):

        opcode_corrente = instrucoes[ip]



        if opcode_corrente.getInstrucao() == "acc":
            opcode_corrente.executar()

            for instrucao in instrucoes:
                if instrucao.getExecucoes()>1:
                    executando=False
                    break

            if executando:
                acc +=opcode_corrente.getArgumento()
                ip+=1
        elif opcode_corrente.getInstrucao() == "jmp":
            opcode_corrente.executar()

            for instrucao in instrucoes:
                if instrucao.getExecucoes()>1:
                    executando=False
                    break

            if executando:
                ip+=opcode_corrente.getArgumento()
        elif opcode_corrente.getInstrucao() == "nop":
            opcode_corrente.executar()

            for instrucao in instrucoes:
                if instrucao.getExecucoes()>1:
                    executando=False
                    break

            if executando:
                ip+=1

        print(str(opcode_corrente) + " - " + str(sequencia) + " ->> IP = " + espacar(str(ip),5) + " ACC = " + espacar(str(acc),5) + " REP = " + espacar(str(opcode_corrente.getExecucoes()),5))

        sequencia+=1

        
    print()
    print("Acumulador : "+str(acc))

def executar(instrucoes):
    ip = 0
    acc = 0
    executando = True

    sequencia = 1


    while(executando):

        if ip >= len(instrucoes):
            terminou = "Fim do Programa"
            break

        opcode_corrente = instrucoes[ip]


        if opcode_corrente.getInstrucao() == "acc":
            opcode_corrente.executar()

            for instrucao in instrucoes:
                if instrucao.getExecucoes()>1:
                    executando=False
                    terminou = "Loop"
                    break

            if executando:
                acc +=opcode_corrente.getArgumento()
                ip+=1
        elif opcode_corrente.getInstrucao() == "jmp":
            opcode_corrente.executar()

            for instrucao in instrucoes:
                if instrucao.getExecucoes()>1:
                    executando=False
                    terminou = "Loop"
                    break

            if executando:
                ip+=opcode_corrente.getArgumento()
        elif opcode_corrente.getInstrucao() == "nop":
            opcode_corrente.executar()

            for instrucao in instrucoes:
                if instrucao.getExecucoes()>1:
                    executando=False
                    terminou = "Loop"
                    break

            if executando:
                ip+=1

        print(str(opcode_corrente) + " - " + str(sequencia) + " ->> IP = " + espacar(str(ip),5) + " ACC = " + espacar(str(acc),5) + " REP = " + espacar(str(opcode_corrente.getExecucoes()),5))

        sequencia+=1

        
    print()
    print("Acumulador : "+str(acc))
    print("Terminou com : " + terminou)

    return terminou

def instrucoes_get_copia(instrucoes):
    copia = []
    for instrucao in instrucoes:
        copia.append(Opcode(instrucao.getInstrucao(),instrucao.getArgumento()))
    
    return copia



def solucao_parte_extra(entradas):

    instrucoes = []

    nop_e_jmp = 0

    for instrucao in entradas:
        tx_instrucao = instrucao.split(" ")[0]
        tx_argumento = instrucao.split(" ")[1]

        instrucoes.append(Opcode(tx_instrucao,int(tx_argumento)))

        if (tx_instrucao == "nop" or tx_instrucao == "jmp"):
            nop_e_jmp+=1

    tentativa = 0

    while(tentativa < nop_e_jmp):
        instrucoes_copia = instrucoes_get_copia(instrucoes)
     
        contagem = 0

        for instrucao in instrucoes_copia:
            if instrucao.getInstrucao() == "nop":
                if(contagem == tentativa):
                    instrucao.setInstrucao("jmp")
                    break
                contagem+=1
            elif instrucao.getInstrucao() == "jmp":
                if(contagem == tentativa):
                    instrucao.setInstrucao("nop")
                    break
                contagem+=1



        print("------ TENTATIVA :: "+str(tentativa+1) + " de " + str(nop_e_jmp))
        resultado = executar(instrucoes_copia)
        if resultado == "Fim do Programa":
            break
        tentativa+=1



main()