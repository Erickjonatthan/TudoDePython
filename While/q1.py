lista= []
soma= 0
num=0
maior=0
while num != -100:
  num=float(input("Informe um valor: "))
  if num != -100:
    lista.append(num)
    soma+=num
    maior= lista[0]
    if num > maior:
      maior = num

if len(lista) > 0:
  media= soma/len(lista)
else:
  media=0
print("=" * 90)
print("Soma: ", soma,"\nMaior número: ",maior,"\nMédia: ",media)