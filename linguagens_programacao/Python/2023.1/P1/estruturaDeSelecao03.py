# Programa: idade.py
# Programador:
# Data: 03/04/2016
# Este programa lê a data de nascimento de uma pessoa e uma data de
# referência e calcula a idade em anos completos da pessoa na data de
# referência. As datas são dadas no formato dd/mm/aaa. O programa
# imprime a idade calculada.
# início do módulo principal
from datetime import date
# descrição das variáveis utilizadas
# int rdia, rmes, rano
# int ndia, nmes, nano
# pré: rdia rmes rano ndia nmes nano
# Passo 1. Leia as datas da entrada
# Passo 1.1. Leia a data de referência
rdia,rmes,rano=map(int,input('Data de referência: ').split('/'))
# print(date.today())
# Passo 1.2. Leia a data do aniversário
ndia,nmes,nano=map(int,input('Data de nascimento: ').split('/'))
# Passo 2. Calcule a idade da pessoa
# Passo 2.1. Calcule a diferença dos anos
idade = rano - nano
# Passo 2.2. Verifique se o mês do aniversário ainda não passou
if nmes > rmes:
   idade = idade - 1
# Passo 2.3. Se o mês atual é o do aniversário verifique o dia
elif nmes == rmes and ndia > rdia:
   idade = idade - 1
# Passo 3. Imprima a idade da pessoa
print('A pessoa tem {0:d} anos completos'.format(idade))
# pós: idade
# fim do módulo principal