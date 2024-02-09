# -*- coding: utf-8 -*-
# Programa: fragmentos.py
# Programador:
# Data: 11/10/2021
# Este programa lê dois conjuntos com m e n fragmentos de DNA,
# computa quantos e quais ocorrem simultaneamente nos dois
# conjuntos e imprime o resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# list amostra1, amostra2, simul
# int tam

# pré: amostra1[0] amostra1[1] .. amostra1[m-1]
#      amostra2[0] amostra2[1] .. amostra2[n-1]

# Passo 1. Leia a entrada
# Passo 1.1. Leia os elementos da amostra1
amostra1 = [str(frag) for frag in input().split()]
# Passo 1.2. Leia os elementos da amostra2
amostra2 = [str(frag) for frag in input().split()]
# Passo 2. Compute quantos e quais fragmentos ocorrem simultaneamente
# Passo 2.1. Compute o tamanho da primeira lista
tam = len(amostra1)
# Passo 2.2. Inclua os elementos da amostra2 em amostra1
amostra1.extend(amostra2)
# Passo 2.3. Inicilize a lista simul e num
simul = []
num = 0
# Passo 2.3. Compute os elementos que aparecem 2 vezes na lista estendida
for i in range(0,tam): 
   if amostra1.count(amostra1[i]) == 2: 
      simul.append(amostra1[i])
      num += 1
# Passo 3. Imprima quantos e a lista dos simultâneos
msg = f'{num} fragmentos: {*simul,}'
print(msg)

# pós: num == Num i em {0..m-1} and j em {0..n-1}:amostra1[i]==amostra2[j]
#      simul == [simul[0],..,simul[k-1]] and k == num and
#      simul[l] em amostra1 and amostra2
# fim do módulo principal