# -*- coding: utf-8 -*-
# Programa: poluicao1.py
# Programador:
# Data: 30/03/2016
# Este programa lê três medidas de poluição, leitura1, leitura2 e
# leitura3. A média dessas três leituras é usada como o índice de poluição
# da cidade, valores desse índice de poluição abaixo de 35 indicam
# condição agradável, valores maiores ou iguais a 35 e menores ou iguais
# a 60 indicam condição desagradável, enquanto valores maiores que 60
# indicam condição perigosa.  O programa calcula o índice de poluição e
# então determina e imprime a condição apropriada, agradável, desagradável
# ou perigosa.
# inicio do módulo principal
# descrição das variáveis utilizadas
# int leitura1, leirura2, leitura3, leitura4
# float indice
# string msg

# pré: leitura1 leitura2 leitura3

# Passo 1. Leia as medidas de poluicao
print('Entre com 3 medidas de poluição: ')
leitura1 = int(input())
leitura2 = int(input())
leitura3 = int(input())
# Passo 2. Calcule o indice de poluicao
indice = (leitura1 + leitura2 + leitura3)/3
# Passo 3. Compute a mensagem apropriada
if indice < 35:
    msg = 'Condição Agradavel'
elif indice <= 60:
    msg = 'Condição Desagradavel'
elif indice > 60:
    msg = 'Condição Perigosa'

# Passo 4. Imprima a mensagem
print('{0}'.format(msg))


# pós: indice == (Soma i em {0,1,2}: leitura[i])/3.0 and
#      (indice < 35 and 'Condição Agradavel') or (indice <=60  and
#      'Condição Desagradavel') or (indice > 60 and 'Condição Perigosa')
# fim do módulo principal