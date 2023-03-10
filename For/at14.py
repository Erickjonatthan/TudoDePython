lista = []
qtd = 0
soma = 0
mult = 1
for i in range(5):
    num = int(input("Digite as 5 numeros: "))
    lista.append(num)
    soma += num
    mult *= num
print(lista)
print(soma)
print(mult)