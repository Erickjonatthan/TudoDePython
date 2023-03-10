num1 = int(input("Digite algum número:" ))
num2 = int(input("Digite algum número:" ))
num3 = int(input("Digite algum número:" ))


if num1 > num2:
  if num1 > num3:
    print("O maior número é o:",num1)

elif num2 > num1:
  if num2 > num3:
    print("O maior número é o",num2)
  
elif num3 > num1:
  if num3 > num2:
    print("O maior número é o",num3)
else:
  print("números iguais")