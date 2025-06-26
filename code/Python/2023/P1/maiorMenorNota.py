# -*- coding: utf-8 -*-
# Programa: intervalo.py
# Programador:
# Data: 29/05/2011
# Este programa lê quatro notas de uma prova, calcula a maior e a
# menor nota e a diferença entre elas e imprime o resultado

# início

# pré: nota1 nota2 nota3 nota4

# Passo 1. Leia as Notas
print('Leia as 4 notas: ')
nota1, nota2, nota3, nota4 = map(float, input().split())
# Passo 2. Calcule a maior e a menor nota
menornota = nota1
maiornota = nota1
# Passo 2.1 Compare as notas
if (nota2 < menornota) and (nota2 < nota3) and (nota2 < nota4):
    menornota = nota2
elif (nota3 < menornota) and (nota3 < nota4):
    menornota = nota3
elif nota4 < menornota:
    menornota = nota4

if (nota2 > maiornota) and (nota2 > nota3) and (nota2 > nota4):
    maiornota = nota2
elif (nota3 > maiornota) and (nota3 > nota4):
    maiornota = nota3
elif nota4 > maiornota:
    maiornota = nota4
# Passo 3. Calcule a variacao entre as notas
intervalo = maiornota - menornota
# Passo 4. Imprima o valor do intervalo
print('Maior nota: {0:4.1f}'.format(maiornota))
print('Menor nota: {0:4.1f}'.format(menornota))
print('Variação  : {0:4.1f}'.format(intervalo))

# pós: maiornota == max{nota1, nota2, nota3, nota4} &&
#      menornota == min{nota1, nota2, nota3, nota4} &&
#      intervalo == maiornota - segmaiornota
# fim