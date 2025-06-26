# Programa: medias.py
# Programador:
# Data: 08/04/2016
# Este programa lê um conjunto de notas variando de 0.0 a 10.0, conta-as e
# calcula a média aritmética das notas. A leitura de uma nota negativa
# indica o final da entrada. O programa imprime o número de notas de notas
# e a média das notas.
# início do módulo principal
# descrição das variáveis utilizadas
# float  nota, media
# int    numnotas

# pré: nota_0..nota_n and para i em {0..n-1}:
#      nota_i >= 0.0 and nota_i <=10.0 and nota_n < 0

# Passo 1. Leia uma nota e inicialize as variáveis
# Passo 1.1. Leia uma nota
print('Entre com uma nota negativa para finalizar.')
nota = float(input('Nota: '))
# Passo 1.2. Inicialize as variáveis soma e numnotas
soma = 0.0
numnotas = 0
# Passo 2. Enquanto a nota lida for maior que zero, repita
while nota >= 0.0:
    # Passo 2.1. Incremente o número de notas lidas
    numnotas = numnotas + 1
    # Passo 2.2. Adicione a nota lida em soma
    soma = soma + nota
    # Passo 2.3. Leia a próxima nota
    nota = float(input('Nota: '))
# Passo 3. Calcule a Média das notas
media = soma / numnotas
# Passo 4. Imprima o resultado
print('{0:d} notas com média = {1:3.1f}'.format(numnotas, media))

# pós: media == (Soma i em {0...n-1}:notat_i)/n and n > 0
#      and numnotas == n
# fim do módulo principal
