import random
k= 0
j= 0
substituidor = []
lista = []
tamanho = 10
for i in range(tamanho):
    num = random.randint(0,10)
    lista.append(num)
print(lista)

for i in range(tamanho):
    if i < tamanho - 1:
        k = i + 1
    for j in range(tamanho):
        if lista[j] > lista[k]:
            substituidor = lista[j]
            lista[j] = lista[k]
            lista[k] = substituidor

print(lista)

##lista = [3, 5, 2, 1, 4]

##for i in range(len(lista)):
  ##  menor = i
    ##for j in range(i+1, len(lista)):
    ##    if lista[j] < lista[menor]:
      ##      menor = j
    ##lista[i]= lista[menor]
    # lista[menor] = lista[i]

##print(lista)
