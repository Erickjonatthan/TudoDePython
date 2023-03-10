valorConta = float(input("Digite o valor da sua conta: "))
formaPag = str(input("Forma de pagamento (dinheiro ou cheque): "))

if formaPag == 'dinheiro' :
  if valorConta >= 100:
    valorConta -= (valorConta * 0.1)
    print("R$",valorConta)
  else:
    print("R$",valorConta)
elif formaPag == 'cheque':
  print("R$",valorConta)
else:
  print("Forma de pagamento inválida")