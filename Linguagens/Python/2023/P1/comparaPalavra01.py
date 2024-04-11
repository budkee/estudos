# -*- coding: utf-8 -*-
# Programa: ordenastr.py
# Programador:
# Data: 26/08/2022
# Este programa lê três strings, ordena em ordem
# não decrescente e imprime os resultados.
# início do módulo principal
# descrição das variáveis utilizadas
# float palavra1, palavra2, palavra2, aux

# pré: palavra1, palavra2, palavra3

# Passo 1. Leia as palavras
palavra1 = str(input())
palavra2 = str(input())
palavra3 = str(input())
# Passo 2. Ordene as palavras
# Passo 2.1 Verificação (1,2)
if palavra1 > palavra2:
    palavra1, palavra2 = palavra2, palavra1
# Passo 2.2 Verificação (2,3)
if palavra2 > palavra3:
    palavra2, palavra3 = palavra3, palavra2
# Passo 2.3 Verificação (1,2)
if palavra1 > palavra2:
    palavra1, palavra2 = palavra2, palavra1
# Passo 3. Imprima os resultados
print('{0:s} {1:s} {2:s}'.format(palavra1, palavra2, palavra3))
# pós: palavra1 <= palavra2 <= palavra3
# fim do módulo principal
