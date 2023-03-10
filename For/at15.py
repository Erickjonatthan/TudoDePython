idade= []
altura = []
for i in range(2):
    print("Pessoa: ",(i+1))
    alt = float(input("Digite a alt: " ))
    idad = int(input("Digite a idade: "))
    idade.append(idad)
    altura.append(alt)
idade_inversa = []
for i in range(2):
    idade_inversa.append(idade[len(idade) - i - 1])
altura_inversa = []
for i in range(2):
    altura_inversa.append(altura[len(altura) - i - 1])
print("Idade inversa ",idade_inversa)
print("Altura inversa ",altura_inversa)