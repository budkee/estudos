# Programa: valorabsoluto.py
# Programador:
# Data: 02/09/2018
# Este programa computa o valor absoluto de um número do tipo float. O
# programa lê um número do tipo float e verifica se o número é maior ou
# igual a zero. Em caso afirmativo, o valor absoluto do número é o próprio
# número, caso contrário, o valor absoluto do número é o valor do número
# multiplicado por -1. O programa imprime o número e o valor absoluto de
# número.
# início do módulo principal
# descrição das variáveis utilizadas
# float x, absx
# pré: x
# Passo 1. Leia um número real
x = float(input())
# Passo 2. Calcule o valor absoluto do número lido
# Passo 2.1. Se x for maior ou igual 0
if x >= 0.0:
   absx = x
# Passo 2.2. Caso contrário
else:
   absx = -x
# Passo 3. Imprima o número e seu valor absoluto
print('|{0:.1f}| == {1:.1f}'.format(x, absx))
# pós: absx == x and x >= 0 or absx == -x
# fim do módulo principal