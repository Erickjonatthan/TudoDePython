
qtd = 0
soma = 0
for i in range(5):
    num = int(input(f"Digite o {i +1} número: "))
    
    soma += num
    qtd += 1
print("soma :", soma)
print("média = ", soma/qtd)
