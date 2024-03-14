# -*- coding: utf-8 -*-
# Programa: intersecao01.py
# Programador:
# Data: 23/10/2019
# Este programa lê duas listas com n e m itens cada, calcula a 
# interseção das listas e imprime o resultado
# início do módulo principal
# descrição as variáveis utilizadas
# list ap1, isd, simul
# int tam1, tam2

# pré: tam1 ap1[0] ap1[1] .... ap1[tam1-1]
#      tam2 (isd[0] isd[1] .... isd[tam2-1]

# Passo 1. Leia a entrada
# Passo 1.1. Leia o tamanho da lista1
tam1 = int(input())
# Passo 1.2. Leia os elementos da lista1
ap1 = list(map(int, input().split()))[:tam1]
# Passo 1.3. Leia o tamanho da lista2
tam2 = int(input())
# Passo 1.4. Leia os elementos da lista
isd = list(map(int, input().split()))[:tam2]
# Passo 2. Calcule a interseção das listas
# Passo 2.1. Inicilize a lista simul
simul = []
# Passo 2.2. Para cada elemento da ap1
for mat in ap1:
# Passo 2.2.1. Verifique se ap1 não está em isd
   if mat in isd:
# Passo 2.2.1.1. Insira num em simul
      simul.append(mat)
# Passo 3. Imprima a lista simul
print(simul)

# pós: para i em {0 .. tam3-1}:simul[i] and
#      simul[i] == ap1[j] == isd[l] 
# fim do módulo principal