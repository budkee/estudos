# -*- coding: utf-8 -*-
# Programa: umidade.py
# Programador:
# Data: 22/09/2016
# Este programa lê três medidas da umidade relativa do ar. A média dessas
# três leituras é usada como a medida de umidade relativa da cidade,
# valores dessa medida de umidade relativa do ar abaixo de 12% indicam
# estado de emergência, valores maiores ou iguais a 12% e menores ou iguais
# a 20% indicam estado de alerta, enquanto valores maiores que 20% e
# menores ou iguais a 30% indicam estado de atenção. Para valores
# superiores a 30% e inferiores a 60% indicam estado aceitável e superiores
# ou iguais a 60% indicam estado ideal. O programa calcula a medida da
# umidade relativa do ar e então determina e imprime o estado apropriado,
# estado de emergência, estado de alerta, estado de atenção, estado
# aceitável ou estado ideal.
# início do módulo principal
# descrição das variáveis utilizadas
# int   medida1, medida2, medida3
# float indice
# str   mensagem

# pré: medida1 medida2 medida3

# Passo 1. Leia Medida1, Medida2, Medida3
medida1 = int(input())
medida2 = int(input())
medida3 = int(input())
# Passo 2. Calcule o índice de umidade e a mensagem apropriada
# Passo 2.1. Calcule o índice
indice = (medida1 + medida2 + medida3)/3
# Passo 2.2. Compute a mensagem apropriada
if indice < 12:
    msg = 'Estado de Emergência'
elif indice <= 20:
    msg = 'Estado de Alerta'
elif indice <= 30:
    msg = 'Estado de Atenção'
elif indice < 60:
    msg = 'Estado Aceitável'
else:
    msg = 'Estado Ideal'
# Passo 3. Imprima o resultado apropriado
print(msg)

# pós: indice == (Soma i em {1,2,3}: UmInt[i])/3.0 and
#      (indice < 12 and 'Estado de Emergência') or (indice <=20  and
#      'Estado de Alerta') or (indice <= 30 and 'Estado de Atenção')
#      or (indice  < 60 and 'Estado Aceitável') or 'Estado Ideal'
# fim do módulo principal
