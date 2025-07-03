# Programa: investimento.py
# Programador:
# Data: 10/10/2016
# Este programa lê o valor a ser investido, a taxa de juros anual, a
# periodicidade da aplicação da taxa de juros e o número de anos que o
# valor ficará aplicado, calcula o rendimento da aplicação usando a dada
# taxa de juros e a periodicidade, bem como o números de anos da aplicação
# início do módulo principal
# descrição das variáveis utilizadas
# float valor, taxa, valorAcum
# int numvezes, anos

# pré: valor taxa numvezes anos

# Passo 1. Leia os dados de entrada
# Passo 1.1. Leia o valor depositado
print('Entre com o valor depositado: R$')
valor = float(input())
# Passo 1.2. Leia a taxa de juros anual
print('Entre com a taxa de juros (na forma decimal):')
taxa = float(input())
# Passo 1.3. Leia o número de vezes que a taxa será aplicada
print('Entre com o periodicidade da aplicação da taxa:')
numvezes = int(input())
# Passo 1.4. Leia o número de anos que o valor será aplicado
print('Entre com o número de anos da aplicação:')
anos = int(input())
# Passo 2. Calcule o valor acumulado
# Passo 2.1. Inicialize o valor acumulado
valorAcum = valor
# Passo 2.2. Repita anos*numvezes
for i in range(1, anos * numvezes + 1):
    # Passo 2.2.1. Atualize o valor acumulado com o rendimento
    valorAcum = valorAcum * (1.0 + taxa / numvezes)
# Passo 3. Imprima o resultado com duas casas decimais
print('O valor acumulado é: R${0:8.2f}'.format(valorAcum))

# pós: valorAcum == valor*(Prod i em {1,..,n}:(1.0 + taxa/numvezes))
#      and n == anos*numvezes
# fim do módulo principal
