#! python3

import random
print('*********************************')
print('Bem vindo ao jogo de Adivinhação!')
print('*********************************')



numero_secreto = random.randrange (1,101)
total_de_tentativas = 3

print(numero_secreto)


for rodada in range(1, total_de_tentativas + 1):
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute_str = int(input("Digite um número entre 1 e 100 : "))
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if chute_str < 1 or chute > 100:
        print("Digite um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")
print("\n Fim do Jogo")
