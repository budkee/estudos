# Programa: semisomador.py
# Programador:
# Data: 30/03/2011
# Este programa lê dois números binários de um dígito em um
# circuito lógico que representa um semi-somador binário e calcula e
# imprime a soma dos dois dígitos binários.
# início do módulo principal
# descrição das variáveis utilizadas
# bool a, b, soma, vaiUm
# pré: a b | a, b em {0, 1}
# Passo 1. Leia dois números binários de 1 dígito
print('Entre com dois valores binários: ')
a = bool(int(input()))
b = bool(int(input()))
# Passo 2. Calcule a soma de dois dígitos binários
# Passo 2.1. Calcule o dígito menos significativo da soma
soma = (a or b) and not(a and b)
# Passo 2.2. Calcule o dígito mais significativo da soma
vaiUm = a and b
# Passo 3. Imprima a soma de dois números binários de 1 dígito
print('{0:1d} + {1:1d} = {2:1d}{3:1d}'.format(a, b, vaiUm, soma))
# pós: vaiUm == a and b soma == (a or b) and not(a and b)
# fim do módulo principal