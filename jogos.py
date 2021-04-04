import forca
import adivinhacao


def escolha_jogo():
    print('*********************************')
    print('Escolha o seu jogo!')
    print('*********************************\n')

    print("(1) Forca - (2) Adivinhação")

    jogo = int(input("Qual Jogo? "))

    if jogo == 1:
        print("Jogando Forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolha_jogo()
