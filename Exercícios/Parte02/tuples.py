# list usa colchetes [] para inicialização, tuple usa parênteses ()
# list é mutável, tuple é imutável

# >>> lista = [4,3,2,1]
# >>> tuple = (4,3,2,1)

dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
print(type(dias))
print(dias)

print("#################\n")

dias.append("Sábado2")
print(type(dias))
print(dias)

# Criando uma tupla
print("\nCriando uma tupla\n")
dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
print(type(dias))
dias.append("Sábado2")