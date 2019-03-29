import random


def jogar():
    imprime_mensagem_abertura()
    palavra = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = obtem_chute_jogador()
        index = 0
        if (chute in palavra):
            marca_chute_correto(palavra, chute, letras_acertadas, index)
            acertou = verifica_se_acertou(letras_acertadas, acertou)
        else:
            erros = erros + 1
            desenha_forca(erros)
        enforcou = erros == 7
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra)
    print("Fim do Jogo")


def imprime_mensagem_abertura():
    print("******************************************************")
    print("********** ******** Jogo da Forca! ********** ******* ")
    print("******************************************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def marca_chute_correto(palavra, chute, letras_acertadas, index):
    for letra in palavra:
        if (chute == letra):
            letras_acertadas[index] = letra
        index = index + 1


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def obtem_chute_jogador():
    chute = input("Qual a letra?")
    chute = chute.strip().upper()
    return chute


def verifica_se_acertou(letras_acertadas, acertou):
    letras_faltando = int(letras_acertadas.count('_'))
    if (letras_faltando == 0):
        acertou = True
    return acertou

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
if (__name__ == "__main__"):
    jogar()
