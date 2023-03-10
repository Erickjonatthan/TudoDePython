soma = 0
valor=1
while valor != 0:
  valor = float(input("Digite o valor do produto: R$"))
  if valor >= 0:
    soma+=valor
  else:
    print("Não processado, digite um valor válido.")
if soma > 1000:
  soma = soma * 0.9 
print("=" * 90)
print("Total a pagar: R$", soma)  