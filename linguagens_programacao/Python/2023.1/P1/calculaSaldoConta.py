# -*- coding: utf-8 -*-
# Programa: saldo.py
# Programador:
# Data: 12/10/2016
# Este programa calcula o saldo da conta corrente de um cliente num
# determinado banco. O seu programa lê o crédito disponível da conta
# corrente, a operação a ser realizada ((D) para depósito ou (S) para
# saque), o valor da operação e calcula o saldo após a operação. O programa
# deve imprimir o saldo disponível após a operação.
# início do módulo principal
# descrição das variáveis utilizadas
# float saldo_Anterior, valor_Operacao, saldo_Atual
# str   operacao

# pré: saldo_Anterior operacao valor_Operacao

# Passo 1. Leia o saldo anterior, a operação e o valor
saldo_Anterior = float(input())
operacao = str(input())
valor_Operacao = float(input())
# Passo 2. Calcule o saldo atual
if operacao.upper() == 'D':
    saldo_Atual = saldo_Anterior + valor_Operacao
elif operacao.upper() == 'S':
    saldo_Atual = saldo_Anterior - valor_Operacao
else:
    saldo_Atual = saldo_Anterior
# Passo 3. Imprima os resultado
print('Saldo Atual: R${0:+10.2f}'.format(saldo_Atual))

# pós: saldo_Atual
# fim do módulo principal