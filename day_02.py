def main():

    print("")
    print("---------- Advent of Code 02 --------------")
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc"
    solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    solucao(obter_entradas("inputs/input_02.txt"))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")
    solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    solucao_parte_extra(obter_entradas("inputs/input_02.txt"))

def obter_entradas(arquivo_caminho):
    dados = []

    arquivo = open(arquivo_caminho)
    for linha in arquivo.readlines():
        dados.append(linha)

    return dados

def transformar_texto_em_entradas(entrada_texto):
    entradas = []
    for linha in entrada_texto.split("\n"):
        entradas.append(linha)
    return entradas;

def solucao(entradas):

    validos = 0

    for entrada in entradas:
        print(entrada)

        minimo = entrada_obter_minimo(entrada)
        maximo = entrada_obter_maximo(entrada)
        letra = entrada_obter_letra(entrada)
        senha = entrada_obter_senha(entrada)

        print("\tMinimo : "+str(minimo))
        print("\tMaximo : "+str(maximo))
        print("\tLetra : "+letra)
        print("\tSenha : "+senha)
        print("\tValido : "+str(senha_valida(senha,letra,minimo,maximo)))

        if(senha_valida(senha,letra,minimo,maximo)):
            validos+=1

           
    print("Validos : "+ str(validos))

def solucao_parte_extra(entradas):

    validos = 0

    for entrada in entradas:
        print(entrada)

        minimo = entrada_obter_minimo(entrada)
        maximo = entrada_obter_maximo(entrada)
        letra = entrada_obter_letra(entrada)
        senha = entrada_obter_senha(entrada)

        print("\tMinimo : "+str(minimo))
        print("\tMaximo : "+str(maximo))
        print("\tLetra : "+letra)
        print("\tSenha : "+senha)
        print("\tValido : "+str(senha_posicao_valida(senha,letra,minimo,maximo)))

        if(senha_posicao_valida(senha,letra,minimo,maximo)):
            validos+=1

           
    print("Validos : "+ str(validos))


def entrada_obter_minimo(entrada):
    texto_numero = "";
    for letra in entrada:
        if(letra=='-'):
            break
        texto_numero = texto_numero + letra;
    return int(texto_numero)

def entrada_obter_maximo(entrada):
    texto_numero = "";
    valido=False
    for letra in entrada:
        if(letra=='-'):
            valido=True;
        elif(letra ==" "):
            break;
        elif(valido==True):
             texto_numero = texto_numero + letra;
    
    return int(texto_numero)

def entrada_obter_letra(entrada):
    texto_letra=''
    valido = False

    for letra in entrada:
        if(valido==False):
            if(letra==' '):
                valido=True
        if(valido==True):
            if(letra==':'):
                break;
            else:
                texto_letra=letra;
    return texto_letra

def entrada_obter_senha(entrada):
    texto_senha=""
    espacos = 0

    for letra in entrada:

        if(espacos==2):
             texto_senha += letra;
    
        if(espacos<2):
            if(letra==' '):
                espacos+=1

       

    return texto_senha


def senha_valida(senha,letra,minimo,maximo):

    contagem = 0;

    for letra_passando in senha:
        if(letra_passando == letra):
            contagem+=1

    if (contagem >=minimo and contagem <=maximo):
        return True
    
    return False

def senha_posicao_valida(senha,letra,minimo,maximo):

    senha_tamanho =len(senha)
    validar =0

    if(minimo>senha_tamanho):
        return False
    if(maximo>senha_tamanho):
        return False
    
    for indice,letra_passando in enumerate(senha):
        indice+=1
        #print("Item : "+ str(indice) + " :: "+ letra_passando)
        if(indice == minimo and letra == letra_passando):
            validar+=1;
        if(indice == maximo and letra == letra_passando):
            validar+=1;

    #print("V = "+str(validar))

    if(validar==1):
        return True
    
    return False




main()