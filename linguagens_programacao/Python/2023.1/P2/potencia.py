# Programa: potencia.py
# Programador:
# Data:
# Este programa lê um número real x e uma potência inteira n >= 0,
# computa o valor de x elevado a n e imprime o resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# float numero, potencia
# int pot

# pré: numero pot

# Passo 1. Leia os valores de numero e pot e inicialize potência
# Passo 1.1. Leia o valor do número
numero = float(input('Leia o valor de numero: '))
# Passo 1.2. Leia o valor do expoente
pot = int(input('Leia o valor da potência: '))
# Passo 2. Calcule o valor da potência
# Passo 2.1. Inicialize o valor de potência
potencia = 1
# Passo 2.2. Para i no intervalo [1,pot]
for i in range(1, pot + 1):
    # Passo 2.2.1. Multiplique potencia por numero
    potencia = potencia * numero
# Passo 3. Imprima o valor da potência
print('{0:f}^{1:d} = {2:f}'.format(numero, pot, potencia))

# pós: potencia == Prod i em {1..pot}: numero
# fim do módulo principal
