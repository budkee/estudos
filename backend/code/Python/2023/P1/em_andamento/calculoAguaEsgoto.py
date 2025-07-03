# -*- coding: utf-8 -*-
# Programa: aguaesgoto.py
# Programador:
# Data: 20/11/2016
# Este programa lê o consumo de água de uma residência
# e calcula a fatura da conta de água e esgoto para as
# residência baseada no consumo de agua. O programa lê o código
# da residência (consumidor), o consumo de água da residência, computa
# a fatura e então imprime uma fatura com o código do consumidor e os
# valores cobrados com mensagens apropriadas.
# início do módulo principal
# descrição das variáveis utilizadas
# int cod_consumidor, consumo
# float fat_agua, fat_esgoto, fat_total

# pré: cod_consumidor consumo

# Passo 1. Leia o código do consumidor e consumo de água
cod_consumidor = int(input())
consumo = int(input())
# Passo 2. Calcule valor da fatura
faixas = {
    'até 20': 2.07,
    'de 0 a 10': 4.45,
    'de 11 a 15': 5.79,
    'de 16 a 20': 5.91,
    'de 21 a 25': 6.54,
    'de 26 a 30': 8.01,
    'de 31 a 50': 9.63,
    'maior que 50': 10.78
}
# Passo 2.1. Calcule o valor da água
fat_agua = 0
if consumo <= 20:
    fat_agua = consumo * faixas['até 20']
else:
    for faixa, valor in faixas.items():
        if faixa == 'até 20':
            fat_agua += 20 * valor
        elif faixa == 'maior que 50':
            fat_agua += (consumo - 50) * valor
        else:
            limite_superior = int(faixa.split()[2])
            if consumo > limite_superior:
                fat_agua += (limite_superior - int(faixa.split()[1])) * valor
            else:
                fat_agua += (consumo - int(faixa.split()[1])) * valor
                break

# Passo 2.2. Calcule o valor de esgoto
fat_esgoto = 0.7 * consumo
# Passo 2.3. Calcule o fatura total
fat_total = fat_agua + fat_esgoto
# Passo 3. Imprima os resultado
print('===========================================')
print('Água e Esgotos Pureza e Limpeza Total Ltda.')
print('Consumidor: {0}'.format(cod_consumidor))
print('Consumo de Água: {0}'.format(consumo))
print('Valor da Água  : R${0:8.2f}'.format(fat_agua))
print('Valor do Esgoto: R${0:8.2f}'.format(fat_esgoto))
print('Valor Total    : R${0:8.2f}'.format(fat_total))
print('===========================================')

# pós: fat_total = fat_agua + fat_esgoto
# fim do módulo principal
