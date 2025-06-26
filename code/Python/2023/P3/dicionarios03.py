# Programa: salario00.py
# Programador:
# Data:

# Este programa lê um conjunto de registros com o número, nome,
# setor, data de ingresso, horas trabalhadas na semana e valor do
# salário por hora e calcula o salário semanal de cada funcionário.
# O programa imprime o número, nome e salário de cada funcionário

# início do módulo principal

# descrição das variáveis utilizadas
# list cadastro, folha, chaves1, chaves2
# int tam

# pré: para i em {0..tam-1}: dados[i]

# Passo 1. Leia a entrada e inicialize as variáveis
# Passo 1.1. Leia o número de funcionários
tam = int(input())

# Passo 1.2. Inicialize as abstrações
chaves1 = ['num', 'nome', 'setor', 'data', 'horas', 'salarioh']
cadastro = [dict.fromkeys(chaves1) for _ in range(tam)]

chaves2 = ['num', 'nome', 'salario']
folha = [dict.fromkeys(chaves2) for _ in range(tam)]

dado = []  # lista para lera a entrada

# Passo 1.3. Leia o o cadastro da empresa
for i in range(tam):

    # Passo 1.3.1. Leia os dados dos funcionário i
    dado = input().split(', ')  # lido como lista de str
    cadastro[i]['num'] = dado[0]
    cadastro[i]['nome'] = dado[1]
    cadastro[i]['setor'] = dado[2]
    cadastro[i]['data'] = dado[3]
    cadastro[i]['horas'] = int(dado[4])  # converte para inteiro
    cadastro[i]['salario'] = float(dado[5])  # converte para float
# Passo 2. Calcule os salários
# Passo 2.1. Calcule o salário do funcionário i
for i in range(tam):
    horasextras = 0.5 * (cadastro[i]['horas'] - 40) * cadastro[i]['salario']
    valor = (cadastro[i]['horas'] * cadastro[i]['salario']) + horasextras
    # Passo 2.1.1. Copia parte da lista de dicionários
    folha[i]['num'] = cadastro[i]['num']
    folha[i]['nome'] = cadastro[i]['nome']
    # Passo 2.1.2. Atualiza um campo na lista de dicionários
    folha[i]['salario'] = valor
# Passo 3. Imprime os resultados
for i in range(tam):
    print('{0:s} '.format(folha[i]['num']), end='')
    print('{0:s} {1:.2f}'.format(folha[i]['nome'], folha[i]['salario']))

    # pós: para i em {0..tam-1}: folha[i] and folha[i]['salario'] ==
    #      cadastro[i]['horas']*cadastro[i]['salarioh'] + horasextras and
    #      horasextras==0.5*(cadastro[i]['horas']–40)*cadastro[i]['salarioh']
    # fim do módulo principal