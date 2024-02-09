import math

# Passo 1: leia as entradas
tam = int(input())
lista = list(map(float, input().split()))

# Passo 2: Calcule a média, variância e o desvio
media = sum(lista) / tam
variancia = sum([(i - media)**2 for i in lista]) / tam
desviopadrao = math.sqrt(variancia)

# Passo 3: imprime os resultados
print("Quantidade de números lidos: ", tam)
print("Média: {0:.2f}".format(media))
print("Variância: {0:.2f}".format(variancia))
print("Desvio Padrão: {0:.2f}".format(desviopadrao))
