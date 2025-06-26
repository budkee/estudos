# -*- coding: utf-8 -*-
# Programa: exlacos01.py
# Programador:
# Data: 11/05/2016
# Este programa demostra o funcionamento das estruturas de
# repetição
#    while
#      e
#    for
# início do módulo principal
# descrição das variáveis utilizadas
# int cont, contador

# pré: cont

# Passo 1. Leia o contador dos laços while e for
cont = int(input())
# Passo 2. Execute o laço while
# Passo 2.1. Inicialize o contador do laço while
contador = cont
# Passo 2.2. Imprima o cabeçalho do laço while
print('laço while       :', end='')
# Passo 2.3. Enquanto contador > 0 faça
while contador > 0:
# Passo 2.3.1. Imprima e atualize o número do contador
   print('{0:3d} '.format(contador), end='')
   contador = contador - 1
# Passo 3. Mude de linha e imprima 1 linha vazia
print('\n')
# Passo 4. Execute o laço while
# Passo 4.1 Inicialize contador for	
contador = cont
# Passo 4.2. Imprima o cabeçalho do laço for
print('laço for         :', end='')
# Passo 4.3. Para contador em [5,0] faça
for i in range (contador, 0, -1):
# Passo 4.3.1. Imprima o número do contador
   print('{0:3d} '.format(i), end='')
# Passo 5. Imprima 1 linha vazia
print('')

# pós: cont == 5
#      laço while       :  5   4   3   2   1 
#
#      laço for         :  5   4   3   2   1 
# fim do módulo principal 
