import forca
import adivinhacao

#Início do curso Python avançado!

def selecionar_jogos():
    print("**********************************************")
    print("*** Bem vindo  | JOGOS | Selecione e jogue ***")
    print("**********************************************")

    print("Selecione: ")
    print("[1] = Jogo da forca")
    print("[2] = Jogo de adivinhação")

    jogo = int(input("Qual jogo você escolhe? "))

    if (jogo == 1):
        print("forca")
        forca.jogar()
    else:
        print("adivinhação")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    selecionar_jogos()