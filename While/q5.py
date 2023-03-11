# Escreva um programa que receba como entrada números inteiros até que o número 0 seja informado. Em seguida, o programa deve exibir a soma dos números que são múltiplos de 3.
n = 1
soma = 0
while n!=0:
  n = float(input("Digite um num:"))
  if n % 3 == 0 and n > 0:
   soma+=n

print(soma)