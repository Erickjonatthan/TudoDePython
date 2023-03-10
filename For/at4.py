lista = []
max_num = int(input("Digite um número: "))
for i in range(4):
    num = int(input("Digite um número: "))
    
    if num > max_num:
        max_num = num

print("O maior número é:", max_num)
