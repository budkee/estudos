# Programa: fracoes00.py
# Programador:
# Data:

# Este programa lê dois números racionais no formato p/q,
# computa o produto na forma p/q e imprime o resultado.

# início do módulo principal

# descrição das variáveis utilizadas
# dict num1{}, num2{}, prod{}
# list num1, num2

# pré: num1/den1 num2/den2

# Passo 1. Leia a entrada e inicialize as variáveis
# Passo 1.1. Inicialize as abstrações
chaves = ['num', 'den']  # chaves do dicionário
num1 = dict.fromkeys(chaves)
num2 = dict.fromkeys(chaves)
prod = dict.fromkeys(chaves)

# Passo 1.2. Leia a primeira fração
num1['num'], num1['den'] = map(int, input().split('/'))

# Passo 1.3. Leia a segunda fração
num2['num'], num2['den'] = map(int, input().split('/'))

# Passo 2. Compute o produto das frações
prod = {i: num1[i] * num2[i] for i in chaves}

# Passo 3. Imprima os resultados
print('{0:d}/{1:d}'.format(prod['num'], prod['den']))

# pós: produto == (num1*num2)/(den1*den2)
# fim do módulo principal