senha = str(input("Digite a senha: "))
while True:
  senha2 = str(input("Digite a senha novamente: "))
  if senha == senha2:
    break
  else:
    print("Senha incorreta!")
print("OK!") 