def jogar():
    print('*********************************')
    print('Bem Vindo ao Jogo de Forca!')
    print('*********************************\n')

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input("Qual a Letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print(f"Encontrei a Letra {chute} na posição {index}")
            index = index + 1

        print("Jogando.....")

    print('*********************************')
    print('Fim do Jogo!')
    print('*********************************\n')


if __name__ == "__main__":
    jogar()
