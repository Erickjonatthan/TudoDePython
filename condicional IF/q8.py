valorConta = float(input("Digite o valor da sua conta: "))
formaPag = str(input("Forma de pagamento (cartão, dinheiro ou cheque): "))

if formaPag == 'dinheiro' :

  if valorConta >= 100:
    valorConta -= (valorConta * 0.1)
    print("R$",valorConta)
  else:
    print("R$",valorConta)


elif formaPag == 'cartão':
  formaPagCart = str(input("Crédito ou débito? "))

  if formaPagCart == 'crédito':
    qtdVezes = int(input("Vai ser em quantas vezes? " ))

    if qtdVezes > 3:
      print("Quantidade de parcelas inválida")

    else:
      valorConta /= qtdVezes
      print(qtdVezes,"parcelas de R$", valorConta)
  
  elif formaPagCart == 'débito':
    print("R$",valorConta)
  
elif formaPag == 'cheque':
  print("R$",valorConta)
else:
  print("Forma de pagamento inválida")