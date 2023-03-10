lista = []
qtd = 0
soma= 0
for i in range(4):
    num = float(int(input("Digite as 4 notas: ")))
    lista.append(num)
    soma += num
    qtd +=1

print("notas :", lista)
print("média = ", round(soma/qtd, 2))

