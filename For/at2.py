from random import random


import random
lista = []
lista_invertida = []
#ler 10 numeros
for i in range(10):
    lista.append(random.randint(0,10))
for i in range(10):
    lista_invertida.append(lista[len(lista) - i - 1])   
print(lista)
print(lista_invertida)



   