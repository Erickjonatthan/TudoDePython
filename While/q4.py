# Escreva um programa que receba como entrada números inteiros até que um número maior que 100 seja digitado. Em seguida, esse programa deve exibir a quantidade de números que são pares e positivos.
n = 0
qtd = 0
while n<=100:
  n = float(input("Digite um num:"))
  if n % 2 == 0 and n > 0:
   qtd+=1

print(qtd)