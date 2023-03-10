from winreg import QueryReflectionKey


frase= input("Digite sua frase: ")
frase = frase.upper()
print(frase)
qtdvogais= 0
vogais = "AEIOU"

for letra in frase:
    
    if letra in vogais:
        qtdvogais+= 1

print(qtdvogais)