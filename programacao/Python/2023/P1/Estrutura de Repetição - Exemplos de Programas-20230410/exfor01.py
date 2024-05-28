# -*- coding: utf-8 -*-
# Programa: exfor01.py
# Programador:
# Data: 11/05/2016
# Este programa gera uma tabela de números, iniciando em 1 
# até o limite superior digitado pelo usuário na forma de 
# uma matriz diagonal inferior.
# início do módulo principal
# descrição das variáveis utilizadas
# int limite, linha, coluna	

# pré: limite

# Passo 1. leia a entrada
print('Entre com o número entre 1 e 9: ')
limite = int(input())
# Passo 2. Para linha em [1,limite] faça	
for linha in range(1, limite + 1):
    # Passo 2.1. Para coluna em [1,linha] faça
    for coluna in range(1, linha + 1):
        # Passo 2.1.1. Imprime as colunas da linha i
        print('{0:1d}'.format(coluna), end='')
    # Passo 2.2. Mude de linha
    print('')

# pós: limite == 9
#      1
#      12
#      123
#      1234
#      12345
#      123456
#      1234567
#      12345678
#      123456789
# fim do módulo principal
