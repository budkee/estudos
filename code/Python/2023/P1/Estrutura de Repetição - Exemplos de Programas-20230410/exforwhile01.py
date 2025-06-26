# -*- coding: utf-8 -*-
# Programa: exforwhile01.py
# Programador:
# Data: 11/05/2016
# Este programa demonstra a utilização do uso do while e
# do for.
# início do módulo principal
# descrição das variáveis utilizadas
# int limite, contLaco, contTeste	

# pré: limite

# Passo 1. Leia o limite 
limite = int(input())
# Passo 2. Execução do laço while de 1 a limite
# Passo 2.1. Imprima o cabeçalho do laço while
print('Laço while:            ', end='')
# Passo 2.2. Inicialize os contadores do laço while
contLaco = 1
contTeste = 0
# Passo 2.3. Enquanto contLaco <= limite incremente contTeste e faça
while contLaco <= limite:
    # Passo 2.3.1. Incremente a variável contTeste
    contTeste = contTeste + 1
    # Passo 2.3.2. Imprima e incremente a variável contLaco
    print('{0:3d}'.format(contLaco), end='')
    contLaco = contLaco + 1
# Passo 2.3.3. Imprima o contLaco e contTeste
print('\nContador do Laço:       {0:3d}'.format(contLaco))
print('Número de Testes:       {0:3d}'.format(contTeste))
# Passo 3. Execução do laço for de 1 a limite
# Passo 3.1. Imprima o cabeçalho do laço for
print('Laço for:       ', end='')
# Passo 3.2. Inicialize os contadores do laço for	
contLaco = 1
contTeste = 0
# Passo 3.3. Para contLaco em [1,limite] incremente contTeste e faça
for contLaco in range(1, limite + 1):
    # Passo 3.3.1. Incremente a variável contTeste
    contTeste = contTeste + 1
    # Passo 3.3.2. Imprima a variável contLaco
    print('{0:3d}'.format(contLaco), end='')
# Passo 4. Imprima contLaco e contTeste
print('\nContador do Laço:       {0:3d}'.format(contLaco))
print('Número de Testes:       {0:3d}'.format(contTeste))

# pós: limite == 10 and
#      Laço while:              1  2  3  4  5  6  7  8  9 10
#      Contador do Laço:        11
#      Número de Testes:        10
#      Laço for       :         1  2  3  4  5  6  7  8  9 10
#      Contador do Laço:        10
#      Número de Testes:        10
# fim do módulo principal
