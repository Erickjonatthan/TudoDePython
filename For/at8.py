soma= 0
lista = []
inicio = int(input("Digite o início do intervalo: "))

fim = int(input("Digite o fim do intervalo: "))

for i in range(inicio, fim):
    if i != inicio:
        lista.append(i)
        soma += i
print(soma)
