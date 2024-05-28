# -*- coding: utf-8 -*-
# Programa: compara01.py
# Programador:
# Data: 29/04/2018
# Este programa lê duas de strings de caracteres contíguos,
# sem o caracte espaço, compara e imprime
# maior se a primeira string for maior lexicograficamente 
# que a segunda, ou imprime menor se a primeira for menor 
# lexicograficamente que a segunda ou imprima igual se
# as strings forem iguais.

# início do módulo principal

# descrição das variáveis utilizadas
# str string1, string2 - strings a serem comparadas
# str compara - comparação das strings

# pré: string1 string2

# Passo 1. Leia as strings.
string1, string2 = input().split() 
# Passo 2. Compare as strings
if string1 > string2:
   compara = 'maior'
elif string1 < string2:
   compara = 'menor'
else:
   compara = 'igual'
# Passo 3. Imprima a resposta
print(compara)

# pós: compara == 'igual' and string1 == string2 or compara == 'maior'
#      and string1 > string2 or compra == 'menor' and string1 < string2
# fim do módulo principal