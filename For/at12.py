import random
lista = []
par = []
impar = []
for i in range(20):
    lista.append(random.randint(1,10))
for num in lista:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print("Lista: ",lista,"\nPares: ", par,"\nImpares :", impar)