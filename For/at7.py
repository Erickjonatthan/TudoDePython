lista = []
inicio = int(input("Digite o início do intervalo: "))

fim = int(input("Digite o fim do intervalo: "))

for i in range(inicio, fim): 
    if i != inicio:
        lista.append(i)
if len(lista) > 0:
    print(lista)
else:
    print("ERROR 404! Não existe intervalo entre esse números inteiros")    
