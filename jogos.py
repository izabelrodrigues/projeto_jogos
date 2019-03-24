import advinhacao
import forca

def escolhe_jogo():
    print("******************************************************")
    print("********** ******** **** Jogos ********** ******* ****")
    print("******************************************************")
    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Selecione o jogo: "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        advinhacao.jogar()

if(__name__=="__main__"):
    escolhe_jogo()
