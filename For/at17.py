temp_media = []
meses= 3
tempo = 0
soma = 0
qtd =0 
m =0
mese_acima_med= []
for i in range(meses):
    temp= float(input(f"Digite a temperatura média do mes {i+1}: "))
    temp_media.append(temp)
    soma+= temp
    
med_anual = soma/meses
print("Temperaturas médias :",temp_media)
print("Média anual: ",med_anual)
for temp in temp_media:
    m+=1
    if temp > med_anual:
     mese_acima_med.append(m)
for m in mese_acima_med:
    if m == 3:
        m = "Janeiro"
print("Indice do mes que passou a media:", mese_acima_med)