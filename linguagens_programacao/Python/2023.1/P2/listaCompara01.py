# -*- coding: utf-8 -*-
# Programa: compara04.py
# Programador:
# Data: 08/07/2016
# Este programa lê pares de strings de caracteres contíguos, 
# sem o caractere espaço, compara e imprime 'igual'
# se as duas strings forem iguais lexicograficamente, 'maior' 
# se a primeira string for maior lexicograficamente que a 
# segunda e 'menor' se a primeira for menor lexicograficamente 
# que a segunda. O programa não pode usar nenhuma função que 
# faça comparação de strings. A função len() pode ser usada

# início do módulo principal

# descrição das variáveis utilizadas
# str palavra1, palavra2, compara
# int tam1, tam2, menor
# bool flag

# pré: palavra1 palavra2 and palavra1 == c[0]c[1]..c[tam1-1]
#      and palavra2 == c[0]c[1]..c[tam2-1] and c[i] == char

# Passo 1. Leia as palavras e compute o tamanho
# Passo 1.1. Leia duas palavras
palavra1, palavra2 = input().split()
# Passo 1.2. Calcule o tamanho das palavras
tam1 = len(palavra1)
tam2 = len(palavra2)
# Passo 2. Compare as palavras
# Passo 2.1. Inicialize as variáveis
flag = True # assuma que as palavras são iguais
i = 0  # inicia na posição 0 das palavras
# Passo 2.2. Compute o tamanho da menor palavra
if tam1 > tam2:
   menor = tam2
else:
   menor = tam1
# Passo 2.3. Enquanto i < menor e iguais compare os i caracteres
while i < menor and flag:
   if palavra1[i] > palavra2[i]:
      compara = 'maior'
      flag = False
   elif palavra1[i] < palavra2[i]:
      compara = 'menor'
      flag = False
   else:
      i = i + 1
# fim while
# Passo 2.4. Se flag, verifique qual palavra tem mais caracteres
if flag:
   if tam1 > tam2:
      compara = 'maior'
   elif tam1 < tam2:
      compara = 'menor'
   else:
      compara = 'igual'
# fim if
# Passo 3. Imprima o resultado
print(compara)

# pós: (compara == 'igual' and tam1 == tam2 and para i em
#      {0..tam1-1}:palavra1[i]==palavra2[i]) or (compara ==
#      'maior' and para i em {0..j-1}:palavra1[i]==palavra2[i]
#      and palavra1[j] > palavra2[j]) or compara == 'menor'
# fim do módulo principal