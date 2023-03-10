import random

num = 0
A =  []
quad= 0
soma= 0
for i in range(10):
    num= random.random()
    quad = num**2
    soma += quad
    A.append(num)
print("Lista:", A)
print("Soma dos quadrados: ",soma)
