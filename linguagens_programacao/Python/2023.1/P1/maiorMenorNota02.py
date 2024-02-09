# -*- coding: utf-8 -*-
# Programa: mnnotas01.py
# Programador:
# Data: 15/09/2016
# Este programa lê uma lista de notas, computa a média das
# notas, a maior e a menor nota. As notas são lidas até que uma
# nota negativa seja lida. O programa imprime a maior, a menor nota e a
# média das notas.
# início do módulo principal
# descrição das variáveis utilizadas
# float nota, maiornota, menornota, somanotas, medianotas
# int numnotas

# pré: nota_1 nota_2 ... nota_n and n > 0 and nota_n < 0
#      and para i em {1,..,n-1}:nota_i >= 0.0 and nota_i <=10.0

# Passo 1. Leia uma nota e inicialize as variáveis
print('Entre com uma nota negativa para finalizar.')
# Passo 1.1. Leia uma nota
nota = float(input(''))
# Passo 1.2. Incialize maiornota, menornota e somanotas
maiornota = 0.0
menornota = 10.0
somanotas = 0
numnotas = 1
# Passo 2. Enquanto nota >= 0.0 faça
while nota >= 0.0:
# Passo 2.1. Calcule a maior nota
    if nota > maiornota:
        maiornota = nota
# Passo 2.2. Calcule a maior nota
    if nota < menornota:
        menornota = nota
# Passo 2.3. Compute a soma das notas
    somanotas += nota # somanotas = nota1 + nota2 + nota3 +...+ notai
    print(somanotas)
# Passo 2.4. Incremente o número de notas lidas
    numnotas += 1
# Passo 2.5. Leia uma nota
    nota = float(input(''))
# fim while
# Passo 3. Calcule a média das notas
medianotas = somanotas/(numnotas-1)
# Passo 4. Imprima os resultados
print('Maior Nota = {0:4.1f}'.format(maiornota))
print('Menor Nota = {0:4.1f}'.format(menornota))
print('Média Notas = {0:4.1f}'.format(medianotas))

# pós: maiornota == max i em {1,...,n-1}: nota_i and n > 0 and
#      menornota == min i em {1,...,n-1}: nota[i] and n > 0 and
#      medianota == (soma i em {1,...,n-1}: nota_i)/n and n > 0
# fim do módulo principal
