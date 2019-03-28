def jogar():
    print("******************************************************")
    print("********** ******** Jogo da Forca! ********** ******* ")
    print("******************************************************")

    arquivo = open("palavras.txt", "r")

    palavra_secreta = "banana".upper()
    enforcou = False
    acertou = False

    letras_acertadas = ["_" for letra in palavra_secreta]
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Qual a letra?")
        chute = chute.strip().upper()
        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
            letras_faltando = int(letras_acertadas.count('_'))
            if (letras_faltando == 0):
                acertou = True
        else:
            erros = erros + 1
        enforcou = erros == 6
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou")
    else:
        print("Você perdeu")
    print("Fim do Jogo")

if(__name__=="__main__"):
    jogar()

