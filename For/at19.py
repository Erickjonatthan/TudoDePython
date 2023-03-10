n = int(input("Digite o número de termos da série de Fibonacci que você deseja gerar: "))

a = 0
b = 1

for i in range(n):
    if i == 0:
        print(a, ", ")
    elif i == 1:
        print(b, ", ")
    else:
        c = a + b
        a, b = b, c
        print(c, ", ")
