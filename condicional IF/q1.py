#recendo os lados 1,2 e 3
lado1 = int(input("Olá, digite o primeiro lado do triângulo: "))

lado2 = int(input("Agora, digite o segundo lado do triângulo: "))

lado3 = int(input("Por último, digite o terceiro lado do triângulo: "))

#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
  print("--- Parabéns seu triângulo existe! ----")
  
  #três lados iguais
  if lado1 == lado2 and lado1 == lado3:
    print("Esse triângulo é equilátero.")

  #quaisquer dois lados iguais
  elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Esse triângulo é Isósceles.")

  #três lados diferentes
  elif lado1 != lado2 and lado1 != lado3:
    print("Esse triângulo é Escaleno.")
    
else:
  print("Esse triângulo não existe")