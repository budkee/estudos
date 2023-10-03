# Programa: mnnotas01.py
# Programador:
# Data: 15/09/2016
# Este algoritmo lê um conjunto de notas, computa a maior, a
# menor e a média das notas e imprime os resultados.
# início do módulo principal
# descrição das variáveis utilizadas
# float nota, maiornota, menornota, medianotas
# int numnotas

# pré: nota_1 nota_2 nota_3 ... nota_k

# Passo 1. Leia uma nota e inicialize as variáveis
# Passo 1.1. Leia uma nota
nota = float(input())
# Passo 1.2. Inicialize as variáveis maiornota, menornota e somanotas
maiornota = 0.0
menornota = 10.0
somanotas = 0.0
numnotas = 0
# Passo 2. Enquanto nota lida >= 0.0 faça
while nota >= 0.0:
    # Passo 2.1. Compute a maior nota entre as notas lidas
    if nota > maiornota:
        maiornota = nota
    # Passo 2.2. Compute a menor nota entre as notas lidas
    if nota < menornota:
        menornota = nota
    # Passo 2.3. Compute a soma das notas lidas
    somanotas = somanotas + nota
    # Passo 2.4. Compute o total de notas lidas
    numnotas += 1
    nota = float(input())
# Passo 3. Compute a média das notas lidas
medianotas = somanotas / numnotas
# Passo 4. Imprima a maior, a menor e a média das notas
print('Maior Nota = {0:4.1f}'.format(maiornota))
print('Menor = {0:4.1f}'.format(menornota))
print('Média Notas = {0:4.1f}'.format(medianotas))

# pós: maiornota == max i em {1, 2, .. k-1}:nota_i and
#      maiornota == min i em {1, 2, .. k-1}:nota_i and
#      medianotas == (Soma i em {1, 2, .. k-1}: nota_i)/numnotas
#      numnotas == k-1 and nota_k < 0
# fim do módulo principal
