def main():

    print("")
    print("---------- Advent of Code 04 --------------")
    print("")

    print(" + INTRODUÇÃO")
    print("")
    entrada_texto = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
    solucao(transformar_texto_em_entradas(entrada_texto))


    print("")
    print(" + PROBLEMA")
    print("")
    solucao(transformar_texto_em_entradas(obter_entradas("inputs/input_04.txt")))


    print("")
    print(" + PROBLEMA EXTRA DA INTRODUÇÃO")
    print("")
    solucao_parte_extra(transformar_texto_em_entradas(entrada_texto))

    print("")
    print(" + PROBLEMA EXTRA")
    print("")
    solucao_parte_extra(transformar_texto_em_entradas(obter_entradas("inputs/input_04.txt")))


def solucao(linhas):

    passaportes = []
    validos_contagem=0

    passaporte_corrente =  Passaporte()
    tem_novo = False

    for linha in linhas:
        #print(linha)
        if linha == "":
            if(len(passaporte_corrente.campos)>0):
                passaportes.append(passaporte_corrente)
            passaporte_corrente = Passaporte()
            tem_novo=False
        else:
            tem_novo=True

            campo_nome = ""
            campo_valor = ""
            is_valor = False

            for campo_letra in linha:
                if(campo_letra == ":"):
                    is_valor = True
                else:
                    if(is_valor):
                        campo_valor +=campo_letra
                    else:
                        campo_nome +=campo_letra


            passaporte_corrente.campos.append(Campo(campo_nome,campo_valor))

    if tem_novo == True:
        passaportes.append(passaporte_corrente)

    for passaporte in passaportes:
        print("-------------------------")
        is_valido = False

        contagem_ecl = 0
        contagem_pid = 0
        contagem_eyr = 0
        contagem_hcl = 0
        contagem_byr = 0
        contagem_iyr = 0
        contagem_hgt = 0
        contagem_cid = 0


        for campo in passaporte.campos:
            print("\t ++ " + campo.nome + " = " + campo.valor)

            if(campo.nome == "ecl"):
                contagem_ecl+=1
            elif(campo.nome == "pid"):
                contagem_pid+=1
            elif(campo.nome == "eyr"):
                contagem_eyr+=1
            elif(campo.nome == "hcl"):
                contagem_hcl+=1
            elif(campo.nome == "byr"):
                contagem_byr+=1
            elif(campo.nome == "iyr"):
                contagem_iyr+=1
            elif(campo.nome == "hgt"):
                contagem_hgt+=1
            elif(campo.nome == "cid"):
                contagem_cid+=1
        
        if(contagem_ecl==1 and contagem_pid==1 and contagem_eyr==1 and contagem_hcl==1 and contagem_byr==1 and contagem_iyr==1 and contagem_hgt==1 and contagem_cid<=1):
            is_valido=True

        print(">> Válido : " + SimOuNao(is_valido))
        if(is_valido):
            validos_contagem+=1

    print("")
    print("Válidos = "+str(validos_contagem))

def solucao_parte_extra(linhas):

    passaportes = []
    validos_contagem=0

    passaporte_corrente =  Passaporte()
    tem_novo = False

    for linha in linhas:
        #print(linha)
        if linha == "":
            if(len(passaporte_corrente.campos)>0):
                passaportes.append(passaporte_corrente)
            passaporte_corrente = Passaporte()
            tem_novo=False
        else:
            tem_novo=True

            campo_nome = ""
            campo_valor = ""
            is_valor = False

            for campo_letra in linha:
                if(campo_letra == ":"):
                    is_valor = True
                else:
                    if(is_valor):
                        campo_valor +=campo_letra
                    else:
                        campo_nome +=campo_letra


            passaporte_corrente.campos.append(Campo(campo_nome,campo_valor))

    if tem_novo == True:
        passaportes.append(passaporte_corrente)

    for passaporte in passaportes:
        print("-------------------------")
        is_valido = False
        is_valido_dados = False

        contagem_ecl = 0
        contagem_pid = 0
        contagem_eyr = 0
        contagem_hcl = 0
        contagem_byr = 0
        contagem_iyr = 0
        contagem_hgt = 0
        contagem_cid = 0

        valido_contagem_ecl = 0
        valido_contagem_pid = 0
        valido_contagem_eyr = 0
        valido_contagem_hcl = 0
        valido_contagem_byr = 0
        valido_contagem_iyr = 0
        valido_contagem_hgt = 0


        for campo in passaporte.campos:
            print("\t ++ " + campo.nome + " = " + campo.valor)

            if(campo.nome == "ecl"):
                contagem_ecl+=1

                if(campo.valor in ("amb","blu","brn","gry","grn","hzl","oth")):
                    valido_contagem_ecl+=1

            elif(campo.nome == "pid"):
                contagem_pid+=1

                if(len(campo.valor)==9):
                    if(campo.valor.isdigit()):
                        valido_contagem_pid+=1

            elif(campo.nome == "eyr"):
                contagem_eyr+=1

                if(len(campo.valor)==4):
                    campo_valor_int = int(campo.valor)
                    if(campo_valor_int>=2020 and campo_valor_int<=2030):
                        valido_contagem_eyr+=1

            elif(campo.nome == "hcl"):
                contagem_hcl+=1

                if(len(campo.valor)==7):
                    cor_valida = 0
                    if(campo.valor.startswith("#")):

                        for i,letra in enumerate(campo.valor):
                            if (i>0):
                                if(letra.isdigit() or (letra=="a" or letra=="b" or letra=="c" or letra=="d" or letra=="e" or letra=="f")):
                                    cor_valida+=1
                    if(cor_valida==6):
                        valido_contagem_hcl+=1




            elif(campo.nome == "byr"):
                contagem_byr+=1

                if(len(campo.valor)==4):
                    campo_valor_int = int(campo.valor)
                    if(campo_valor_int>=1920 and campo_valor_int<=2002):
                        valido_contagem_byr+=1


            elif(campo.nome == "iyr"):
                contagem_iyr+=1

                if(len(campo.valor)==4):
                    campo_valor_int = int(campo.valor)
                    if(campo_valor_int>=2010 and campo_valor_int<=2020):
                        valido_contagem_iyr+=1

            elif(campo.nome == "hgt"):
                contagem_hgt+=1

                campo_parte_inteiro = ""

                for letra_valor in campo.valor:
                    if letra_valor.isdigit():
                        campo_parte_inteiro+=letra_valor;
                    else:
                        break

                if(campo.valor.endswith("cm")):
                    campo_parte_inteiro=int(campo_parte_inteiro)
                    if (campo_parte_inteiro>=150 and campo_parte_inteiro<=193):
                        valido_contagem_hgt+=1

                elif (campo.valor.endswith("in")):
                    campo_parte_inteiro=int(campo_parte_inteiro)
                    if (campo_parte_inteiro>=59 and campo_parte_inteiro<=76):
                        valido_contagem_hgt+=1



            elif(campo.nome == "cid"):
                contagem_cid+=1
        
        if(contagem_ecl==1 and contagem_pid==1 and contagem_eyr==1 and contagem_hcl==1 and contagem_byr==1 and contagem_iyr==1 and contagem_hgt==1 and contagem_cid<=1):
            is_valido=True
        
        if(valido_contagem_ecl==1 and valido_contagem_pid==1 and valido_contagem_eyr==1 and valido_contagem_hcl==1 and valido_contagem_byr==1 and valido_contagem_iyr==1 and valido_contagem_hgt==1):
            is_valido_dados=True

        valido_geral = False

        if(is_valido and is_valido_dados):
            valido_geral=True 


        print(">> Válido : " + SimOuNao(valido_geral))
        print(">> Válido P1 : " + QualFalhouP1(contagem_ecl,contagem_pid,contagem_eyr,contagem_hcl,contagem_byr,contagem_iyr,contagem_hgt,contagem_cid))
        print(">> Válido P2 : " + QualFalhouP2(valido_contagem_ecl,valido_contagem_pid,valido_contagem_eyr,valido_contagem_hcl,valido_contagem_byr,valido_contagem_iyr,valido_contagem_hgt))

        print(">> Soma P1 : " + str(SOMATORIO(contagem_ecl,contagem_pid,contagem_eyr,contagem_hcl,contagem_byr,contagem_iyr,contagem_hgt,contagem_cid)))
        print(">> Soma P2 : " + str(SOMATORIO(valido_contagem_ecl,valido_contagem_pid,valido_contagem_eyr,valido_contagem_hcl,valido_contagem_byr,valido_contagem_iyr,valido_contagem_hgt)))

        if(valido_geral):
            validos_contagem+=1

    print("")
    print("Válidos = "+str(validos_contagem))

class Campo:
    def __init__(self,nome,valor):
        self.nome  = nome
        self.valor = valor

class Passaporte:
    def __init__(self):
        self.campos = []


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

def SimOuNao(valor):
    if(valor==True):
        return "Sim"
    else:
        return "Não"


def QualFalhouP1(contagem_ecl,contagem_pid,contagem_eyr,contagem_hcl,contagem_byr,contagem_iyr,contagem_hgt,contagem_cid):

    if contagem_ecl<1:
       return "Erro : ECL"
    elif contagem_pid<1:
       return "Erro : PID"
    elif contagem_eyr<1:
       return "Erro : EYR"
    elif contagem_hcl<1:
       return "Erro : HCL"
    elif contagem_byr<1:
       return "Erro : BYR"
    elif contagem_iyr<1:
       return "Erro : IYR"
    elif contagem_hgt<1:
       return "Erro : HGT"
    else:
        return "OK"
 
    return "DESCONHECIDO"

def QualFalhouP2(contagem_ecl,contagem_pid,contagem_eyr,contagem_hcl,contagem_byr,contagem_iyr,contagem_hgt):

    if contagem_ecl<1:
       return "Erro : ECL"
    elif contagem_pid<1:
       return "Erro : PID"
    elif contagem_eyr<1:
       return "Erro : EYR"
    elif contagem_hcl<1:
       return "Erro : HCL"
    elif contagem_byr<1:
       return "Erro : BYR"
    elif contagem_iyr<1:
       return "Erro : IYR"
    elif contagem_hgt<1:
       return "Erro : HGT"
    else:
        return "OK"
 
    return "DESCONHECIDO"


def SOMATORIO(*contagens):
    somatorio = 0
    for item in contagens:
        somatorio+=item

    return somatorio


main()