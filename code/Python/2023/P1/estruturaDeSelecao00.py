# Programa: poluicao01.py
# Programador:
# Data: 30/03/2011
# Este programa lê três medidas de poluição, leitura1, leitura2, leitura3,
# dadas por números inteiros, o valor limite (LIMITE) e calcula um índice
# de poluição,um número real. Se o valor do índice for menor que LIMITE,
# uma mensagem indicando 'Condição Segura' será impressa; caso contrário,
# uma mensagem indicando 'Condição Perigosa será impressa.
# início do módulo principal
# descrição das variáveis e constantes utilizadas
# LIMITE = 50.0
# int leitura1, leitura2, leitura3
# float indice
# str msg
# pré: LIMITE leitura1 leitura2 leitura3
# Passo 1. Leia a entrada
# Passo 1.1. Defina a constante do valor limite
LIMITE = 50
# Passo 1.2. Leia três medidas de poluição
leitura1 = int(input('Entre com a primeira medida de poluição: '))
leitura2 = int(input('Entre com a segunda medida de poluição: '))
leitura3 = int(input('Entre com a terceira medida de poluição: '))
# Passo 2. Calcule o índice de poluição e a mensagem associada
# Passo 2.1. Calcule o índice de poluição
indice = (leitura1 + leitura2 + leitura3)/3.0
# Passo 2.2. Compute a mensagem relativa ao índice de poluição
# Passo 2.2.1. Se indice menor que o LIMITE atribua 'Condição Segura'
if indice < LIMITE:
   msg = 'Condição Segura'
# Passo 2.2.2. Caso contrário atribua 'Condição Perigosa'
else:
   msg = 'Condição Perigosa'
# Passo 4. Imprima a mensagem
print(msg)
# pós: (Soma i em {1,2,3}: leitura[i])/3.0 < LIMITE and
#      msg == 'Condição Segura' or msg == 'Condição Perigosa'
# fim do módulo principal