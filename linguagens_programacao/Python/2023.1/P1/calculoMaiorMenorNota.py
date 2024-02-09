# -*- coding: utf-8 -*-
# Programa: intervalo.py
# Programador:
# Data: 29/05/2016
# Este programa lê quatro notas de uma prova, calcula a maior e a
# menor nota e a diferença entre elas e imprime o resultado
# início do módulo principal
# descrição das variáveis utilizadas
# float nota1, nota2, nota3, nota4
# float maiornota, menornota, intervalo

# pré: nota1 nota2 nota3 nota4

# Passo 1. Leia as Notas
nota1, nota2, nota3, nota4 = map(float, input().split())
nota = [nota1, nota2, nota3, nota4]
maior = 0
menor = 0
# Passo 2. Calcule a maior e a menor nota
for i in range(len(nota)):
    if nota[i] > maior:
        maior = nota[i]
    elif nota[i] < menor:
        menor = nota[i]

print(maior, menor)
# Passo 3. Calcule a variacao entre as notas
intervalo = maior - menor
# Passo 4. Imprima o valor do intervalo
print('Maior nota: {0:4.1f}'.format(maior))
print('Menor nota: {0:4.1f}'.format(menor))
print('Variação  : {0:4.1f}'.format(intervalo))

# pós: maiornota == max{nota1, nota2, nota3, nota4} and
#      menornota == min{nota1, nota2, nota3, nota4} and
#      intervalo == maiornota - segmaiornota
# fim do módulo principal
