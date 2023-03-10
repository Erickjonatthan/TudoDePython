import random
lista = []
qtdPar = 0
qtdImpar = 0
for i in range(10):
    lista.append(random.randint(1,10))
for num in lista: 
    if num % 2 == 0:
        qtdPar+= 1
    else:
        qtdImpar+=1
print(lista)
print("Quantidade de numeros impares: ", qtdImpar)

print("Quantidade de numeros pares: ", qtdPar)
