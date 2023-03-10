#recebe os 3 tipos de lavagem, pois são 3 pedidos
tipoLavagem1 = int(input("PEDIDO (1) Digite seu tipo de lavagem: 1 p/ peça ; 2 p/peso: "))
tipoLavagem2 = int(input("\nPEDIDO (2) Digite seu tipo de lavagem: 1 p/ peça ; 2 p/peso: "))
tipoLavagem3 = int(input("\nPEDIDO (3) Digite seu tipo de lavagem: 1 p/ peça ; 2 p/peso: "))
#cria uma lista para armazenar o valor de cada pedido
valorPedidos = []
#cria uma lista para armazenar a qtd de secos
secos = []

#se o pedido 1 for a peça
if tipoLavagem1 == 1 :
  print("\n--- TIPO PEÇA ---- (PEDIDO1)")
  #recebe quantas pecas são
  qtdPecas = int(input("Qual a quantidade de peças? "))
  #pergunta se é a seco
  lavagemSeco = str(input("A lavagem vai ser a seco? 's' p sim ; 'n' p/ não "))
  #se a resposta for sim 
  if lavagemSeco == 's': 
    #adiciona um valor aleatório a secos ja que o que vai contar vai ser o tamanho
    secos.append(1)

    cobrancaPeca = 7 * qtdPecas
    taxa = 3.50 * qtdPecas

    valPecaSeco = cobrancaPeca + taxa
    #armazena o valor do pedido a seco de peça no valorPedidos
    valorPedidos.append(valPecaSeco)
  #se for não
  elif lavagemSeco == 'n':
    valPecaSeco = 7 * qtdPecas
    #armazena o valor do pedido de peça no valorPedidos
    valorPedidos.append(valPecaSeco)
#se o pedido 1 for a quilo
if tipoLavagem1 == 2:
  print("\n--- TIPO PESO --- (PEDIDO1)")

  #recebe quantos quilos de roupa
  qtdKg = int(input("Quantos quilos de roupa? "))

  #pergunta se é a seco
  lavagemSeco = str(input("A lavagem vai ser a seco? 's' p sim ; 'n' p/ não "))

  #se a resposta for sim 
  if lavagemSeco == 's': 
    #adiciona um valor aleatório a secos ja que o que vai contar vai ser o tamanho
    secos.append(1)
    cobrancaKg = 5 * qtdKg
    taxa = 3.50 * qtdKg
    valKgSeco = cobrancaKg + taxa
    #armazena o valor do pedido a seco de quilos no valorPedidos
    valorPedidos.append(valKgSeco)
  #se for não
  elif lavagemSeco == 'n':
    valKgSeco = 5 * qtdKg
    #armazena o valor do pedido de quilos no valorPedidos
    valorPedidos.append(valKgSeco)

#se o pedido 2 for a peca (Do pedido 1 para o 2 e 3 é a mesma coisa...)
if tipoLavagem2 == 1 :
  print("\n--- TIPO PEÇA ---- (PEDIDO2)")
  qtdPecas = int(input("Qual a quantidade de peças? "))
  lavagemSeco = str(input("A lavagem vai ser a seco? 's' p sim ; 'n' p/ não "))
  if lavagemSeco == 's': 
    secos.append(1)
    cobrancaPeca = 7 * qtdPecas
    taxa = 3.50 * qtdPecas
    valPecaSeco = cobrancaPeca + taxa
    valorPedidos.append(valPecaSeco)
  elif lavagemSeco == 'n':
    valPecaSeco = 7 * qtdPecas
    valorPedidos.append(valPecaSeco)

#se o pedido 2 for a quilo 
if tipoLavagem2 == 2:
  print("\n--- TIPO PESO --- (PEDIDO2)")
  qtdKg = int(input("Quantos quilos de roupa? "))
  lavagemSeco = str(input("A lavagem vai ser a seco? 's' p sim ; 'n' p/ não "))
  if lavagemSeco == 's': 
    secos.append(1)
    cobrancaKg = 5 * qtdKg
    taxa = 3.50 * qtdKg
    valKgSeco = cobrancaKg + taxa
    valorPedidos.append(valKgSeco)
  elif lavagemSeco == 'n':
    valKgSeco = 5 * qtdKg
    valorPedidos.append(valKgSeco)
#se o pedido 3 for a peca
if tipoLavagem3 == 1 :
  print("\n--- TIPO PEÇA ---- (PEDIDO3)")
  qtdPecas = int(input("Qual a quantidade de peças? "))
  lavagemSeco = str(input("A lavagem vai ser a seco? 's' p sim ; 'n' p/ não "))
  if lavagemSeco == 's': 
    secos.append(1)
    cobrancaPeca = 7 * qtdPecas
    taxa = 3.50 * qtdPecas
    valPecaSeco = cobrancaPeca + taxa
    valorPedidos.append(valPecaSeco)
  elif lavagemSeco == 'n':
    valPecaSeco = 7 * qtdPecas
    valorPedidos.append(valPecaSeco)

#se o pedido 3 for a quilo
if tipoLavagem3 == 2:
  print("\n--- TIPO PESO --- (PEDIDO3)")
  qtdKg = int(input("Quantos quilos de roupa? "))
  lavagemSeco = str(input("A lavagem vai ser a seco? 's' p sim ; 'n' p/ não "))
  if lavagemSeco == 's': 
    secos.append(1)
    cobrancaKg = 5 * qtdKg
    taxa = 3.50 * qtdKg
    valKgSeco = cobrancaKg + taxa
    valorPedidos.append(valKgSeco)
  elif lavagemSeco == 'n':
     valKgSeco = 5 * qtdKg
     valorPedidos.append(valKgSeco)

#calcula o total arrecadado no final
totalArrecadado = valorPedidos[0] + valorPedidos[1] + valorPedidos[2]

#pega o tamanho da lista de secos
qtdSecos = len(secos)

#exibe tudo para o usuario
print("\nValor do pedido 1: ", valorPedidos[0],"R$")
print("Valor do pedido 2: ", valorPedidos[1],"R$")
print("Valor do pedido 3: ", valorPedidos[2],"R$")
print("\nTotal arrecadado para a lavanderia: ",totalArrecadado,"R$")
print("\nA quantidade de lavagem a seco solicitada: ", qtdSecos)