import random

# Inicializa uma lista de contadores com zeros
contadores = [0, 0, 0, 0, 0, 0]

# Laço para simular 100 lançamentos de dados
for i in range(100):
    dado = random.randint(1, 6)
    contadores[dado - 1] += 1

# Laço para mostrar o resultado
for i in range(len(contadores)):
    print(f"O valor {i + 1} foi conseguido {contadores[i]} vezes.")
