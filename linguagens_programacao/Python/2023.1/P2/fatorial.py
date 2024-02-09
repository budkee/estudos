x  # Programa: fatorial01.py
# Programador:
# Data: 28/04/2016
# Este programa lê um número natural, computa e imprime o
# fatorial do número.
# início do módulo principal
# descrição das variáveis utilizadas
# int numero, fatorial
# int i
# pré: numero >= 0
# Passo 1. Leia o valor do número
numero = int(input('Entre com o número: '))
# Passo 2. Calcule o fatorial de número
# Passo 2.1. Compute o fatorial de 0
fatorial = 1
# Passo 2.2. Para i no intervalo (1, numero+1, 1) faça
for i in range(1, numero + 1):
    # Passo 2.2.1. Compute o fatorial de i
    fatorial = fatorial * i  # fatorial acumula o produto
# Passo 3. Imprima o valor do fatorial
print('O fatorial de {0} é {1}'.format(numero, fatorial))
# pós: fatorial == Prod i em {1,...,numero}: i
# fim do módulo principal
