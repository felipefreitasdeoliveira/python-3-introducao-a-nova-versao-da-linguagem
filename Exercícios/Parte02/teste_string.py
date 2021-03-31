palavra = "banana"
palavra2 = "CASA"
print(str.capitalize(palavra))
print(str.casefold(palavra2))
print(str.upper(palavra))
print(str.isnumeric(palavra2))

felipe = str.casefold(input('Digite a palavra: ?' ))
print(felipe)

felipe = str.strip(str.casefold(input('Digite a palavra: ?' )))
print(felipe)