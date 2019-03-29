import random


def imprime_mensagem_abertura():
    print("******************************************************")
    print("********** ***** Jogo de adivinhação! ********** *****")
    print("******************************************************")


def define_nivel_dificuldade():
    print("Nivel de dificuldade: (1) - fácil -- (2) - médio -- (3) - difícil ")
    dificuldade = int(input("Defina a dificuldade:  "))
    return dificuldade


def calcula_numero_tentativas(dificuldade):
    if (dificuldade == 1):
        total_de_tentativas = 15
    elif (dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    return  total_de_tentativas


def jogar():
    imprime_mensagem_abertura()
    pontuacao = 1000
    total_de_tentativas = 0
    numero_secreto = random.randrange(1, 101)

    dificuldade = define_nivel_dificuldade()
    total_de_tentativas = calcula_numero_tentativas(dificuldade)

    # rodada = 1

    # while (rodada <= total_de_tentativas):
    #     print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    #
    #     chute_str = input("Digite seu número: ")
    #
    #     chute = int(chute_str)
    #
    #     acertou = chute == numero_secreto
    #     maior = chute > numero_secreto
    #     menor = chute < numero_secreto
    #
    #     print("Você digitou ", chute)
    #
    #     if acertou:
    #         print("Voçê acertou")
    #     else:
    #         if maior:
    #             print("Você errou. Seu chute é maior que o número secreto!")
    #         elif menor:
    #             print("Você errou. Seu chute é menor que o número secreto!")
    #
    #     rodada = rodada + 1

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100:  ")

        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print("Você digitou ", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if acertou:
            print("Voçê acertou e fez {} pontos!".format(pontuacao))

            break
        else:
            if maior:
                print("Você errou. Seu chute é maior que o número secreto!")
            elif menor:
                print("Você errou. Seu chute é menor que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontuacao = pontuacao - pontos_perdidos
    print("Fim do Jogo")

if(__name__=="__main__"):
    jogar()

