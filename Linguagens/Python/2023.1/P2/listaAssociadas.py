# -*- coding: utf-8 -*-
# Programa: umidade.py
# Programador:
# Data: 25/10/2019
# Este programa lê as umidades relativas do ar às 12:00 horas de cada dia
# da semana e calcula a média é imprime os dias da semana que a
# umidade é maior que a média.
# início do módulo principal
# descrição das variáveis utilizadas
# list dias, umidade
# list maior
# float media

# pré: umidade[0],..., umidade[6]

# Passo 1. Leia a entrada
# Passo 1.1. Inicialize a lista dos dias da semana
dias = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
# Passo 1.2. Leia as umidades dos dias da semana
umidade = list(map(float, input().split()))[:7]
# Passo 2. Calcule a média da semana
media = sum(umidade)/7.0
# Passo 3. Verifique os dias que a umidade é maior que a média
maior = [] # inicialize uma lista vazia
# Passo 3.1. Verifique se a umidade do dia é maior que a média
for dia in dias:
   if umidade[dias.index(dia)] > media:
      maior.append(dia)
# Passo 4. Imprima o resultado
print(maior)

# pós: maior | maior[i] > media
# fim do módulo principal