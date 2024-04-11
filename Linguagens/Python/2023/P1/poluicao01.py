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
qualiBoa = 50 # Abaixo de 50: Qualidade do Ar Boa
qualiRegular = 100 # (>=) Maior ou igual a 50 and (<=) menores ou iguais a 100
qualiInadequada = 200 # (>) Maior que 100 and (<=) Menor ou igual a 200
qualiRuim = 300 #
qualiPessima = 300

# Passo 1.2. Leia três medidas de poluição
leitura1, leitura2, leitura3, leitura4 = map(float, input('').split())
# Passo 2. Calcule o índice de poluição e a mensagem associada
# Passo 2.1. Calcule o índice de poluição
indice = (leitura1 + leitura2 + leitura3 + leitura4)/4.0 # 35
# Passo 2.2. Compute a mensagem relativa ao índice de poluição
# Passo 2.2.1. Se indice menor que o LIMITE atribua 'Condição Segura'

if indice <= 50: #qualiBoa
   msg = 'Qualidade do Ar Boa'
elif indice <= 100:
   msg = 'Qualidade do Ar Regular'
elif indice < 200:
   msg = 'Qualidade do Ar Inadequada'
elif indice < 300:
   msg = 'Qualidade do Ar Ruim'
else:
   msg = 'Qualidade do Ar Péssima'
# Passo 4. Imprima a mensagem
print('Indice: {} = {}'.format(indice, msg))
# pós: (Soma i em {1,2,3,4}: leitura[i])/4.0 < LIMITE and
#      msg == 'Condição Segura' or msg == 'Condição Perigosa'
# fim do módulo principal