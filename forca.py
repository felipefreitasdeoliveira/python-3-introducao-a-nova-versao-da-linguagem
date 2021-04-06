def jogar():
    print('*********************************')
    print('Bem Vindo ao Jogo de Forca!')
    print('*********************************\n')

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    total_erros = 3

    # while True:
    #     total_erros = input("Quantas Vezes quer errar?:")
    #     if total_erros.isnumeric():
    #         print('Voce digitou o numero ' + total_erros)
    #         break
    #     else:
    #         #continue
    #         print("Apenas numero por favor")
    #         #se quiser coloque uma mensagem de erro

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input("Qual a Letra? ")
        chute = chute.strip().upper()
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, vc errou! Faltam {total_erros - erros} tentativas")

        enforcou = erros == total_erros
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)
    if acertou:
        print('\nParabéns você acertou!\n')
    else:
        print('\nQue pena você errou!\n')
    print('*********************************')
    print('Fim do Jogo!')
    print('*********************************\n')


if __name__ == "__main__":
    jogar()
