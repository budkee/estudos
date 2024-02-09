# -*- coding: utf-8 -*-
# Programa: embalagensb.py -- versao boca
# Programador:
# Data: 03/04/2011
# Este programa lê o número de chocolates a serem enviados. Calcula a
# forma como os chocolates devem ser embalados. Como os chocolates são
# frágeis, nenhuma caixa pode ficar com espaçoo vazio, pois isso pode
# danificar as barras de chocolates. Serao utilizadas quatro tamanhos de
# embalagens: enorme, grande, medio e pequeno, as quais podem conter 50,
# 20, 5 e 1 barras de chocolate, respectivamente. O programa calcula
# numero de caixas de tamanho enorme, grande, medio e pequeno,
# necessarias para enviar o numero de chocolates lidos utilizando o
# minimo de caixas. O programa imprime a quantidade de caixas
# necessarias para o envio dos chocolates. Sao enviados no maximo 30.000
# barras de chocolate.
# inicio do módulo principal
# int ENORME, GRANDE, MEDIO, PEQUENO
# int numchocolates, cxenorme, cxgrande, cxmedia, cxpequena

# pré: numchocolates

# Passo 1. Inicialize as constantes e leia o num de barras de chocolate
# Passo 1.1. Inicialize as constantes
ENORME = 50
GRANDE = 20
MEDIO = 5
PEQUENO = 1
# Passo 1.2. Leia os número de barras de chocolates
# print('Entre com o número de barras de chocolate: ')
numchocolates = int(input(''))
# Passo 2. Calcule o número de embalagens
# Passo 2.1. Calcule o número de embalagens de tamanho enorme
cxenorme = numchocolates // ENORME
                           # número de barras sem embalagem
# Passo 2.2. Calcule o número de embalagens de tamanho grande
cxgrande = (numchocolates % ENORME) // GRANDE
                           # número de barras sem embalagem
# Passo 2.3. Calcule o número de embalagens de tamanho médio
cxmedia = (numchocolates % GRANDE) // MEDIO
                           # número de barras sem embalagem
# Passo 2.4. Calcule o número de embalagens de tamanho pequeno
cxpequena = (numchocolates % MEDIO) // PEQUENO
                           # número de barras sem embalagem
# Passo 3. Imprime os resultados
print(' Caixa        Qtde')
print('===========   =====')
print('  Enorme       {0:3d}'.format(cxenorme))
print('  Grande       {0:3d}'.format(cxgrande))
print('  Média        {0:3d}'.format(cxmedia))
print('  Pequena      {0:3d}'.format(cxpequena))

# pós: cxenorme, cxgrande, cxmedio, cxpequena
# fim do módulo principal
