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
        enforcou = erros == 6
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()
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
    print("Você ganhou!")


def imprime_mensagem_perdedor():
    print("Você perdeu!")


if (__name__ == "__main__"):
    jogar()
