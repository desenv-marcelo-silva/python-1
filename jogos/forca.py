def jogar():
    print("**********************************")
    print("*** Bem vindo ao jogo da forca ***")
    print("**********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Qual a letra? ")

        posicao = 0
        for letra in palavra_secreta:
            posicao = posicao + 1
            if (letra == chute):
                print("A letra {} foi encontrada na posição {}".format(chute, posicao))

    print("Fim de jogo.")

if (__name__ == "__main__"):
    jogar()