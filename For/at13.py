# Define o número de alunos
num_alunos = 5

# Inicializa uma lista para armazenar as médias de cada aluno
medias = []

# Laço para pegar as notas de cada aluno
for i in range(num_alunos):
    print(f"Entre com as notas do aluno {i + 1}:")

    # Pega as quatro notas do aluno
    lista = []
    qtd = 0
    soma= 0
    for i in range(4):
        num = float(int(input("Digite as 4 notas: ")))
        lista.append(num)
        soma += num
        qtd +=1
    media= round(soma/qtd, 2)
    print("notas :", lista)
    print("média = ",media)




    # Calcula a média do aluno
    
    # Adiciona a média a lista
    medias.append(media)

# Inicializa uma variável para contar o número de alunos com média >= 7.0
contador = 0

# Laço para percorrer as médias e verificar se são >= 7.0
for media in medias:
    if media >= 7.0:
        contador += 1

# Imprime o resultado
print(f"Número de alunos com média >= 7.0: {contador}")
