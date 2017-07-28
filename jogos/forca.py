def jogar():
    print("**********************************")
    print("*** Bem vindo ao jogo da forca ***")
    print("**********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    letras_acertadas = ["_","_","_","_","_","_"]
    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip().lower()

        posicao = 0
        for letra in palavra_secreta:
            if letra.lower() == chute:
                letras_acertadas[posicao] = letra
            posicao = posicao + 1

    print(letras_acertadas)
    print("Fim de jogo.")

if (__name__ == "__main__"):
    jogar()