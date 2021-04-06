# list usa colchetes [] para inicialização, tuple usa parênteses ()
# list é mutável, tuple é imutável

# >>> lista = [4,3,2,1]
# >>> tuple = (4,3,2,1)
p1 = (3, 5, "Casa")
p2 = (4, 6)
p3 = (5, 7)

line = [p1, p2, p3]
x = p1[2].upper()
print(x)
print(type(line))
print(line[0])

print(line[2])
print(line[0], [2])

print("\n Aqui é Tupla \n")
tupla = (1,2,3,4,5,6,6,7)
print(tupla)
print(type(tupla))
print("\n Cconvertendo para lista \n")
convert_tupla = list(tupla)
print(convert_tupla)
print(type(convert_tupla))

print("\n Tratando Listas \n")
lista = [11122233344, 22233344455, 33344455566]
lista.append(11122233344) #funciona!
print(lista)
print('-----------------------------')
lista2 = {11122233344, 22233344455, 33344455566, "casa", 0, -100}
lista2.add(11122233344) #funciona!
print(lista2)

for cpf in lista2:
     print(cpf)