# -*- coding: utf-8 -*-
# Programa: primeiroultimo.py
# Programador:
# Data: 03/05/2016
# Este programa lê um número inteiro e computa se o primeiro e o
# último número são iguais.
# início do módulo principal
# descrição das variáveis utilizadas
# int numero, ultimo, primeiro, digito
# str msg

# pré: numero

# Leitura da entrada:
numero = int(input())

# Inicialização das variáveis primeiro e ultimo
primeiro = numero
ultimo = numero % 10

# Percorre os dígitos do número
while primeiro >= 10:
    primeiro = primeiro // 10

# Verifica se o primeiro e o último dígitos são iguais
if primeiro == ultimo:
    msg = 'sim'
else:
    msg = 'não'
# Passo 3. Imprima o resultado
print(msg)

# pós: 'sim' and numero[0] == numero[n-1] or 'não'
# fim do módulo principal
