# Programa: lucro00.py
# Programador:
# Data:

# Este algoritmo lê um conjunto de registros com o número, nome,
# estoque, preço de custo e preço de venda e calcula o lucro provável
# de cada item se todo o estoque for vendido e o lucro provável total

# início do módulo principal

# descrição das variáveis e abstrações utilizadas
# list estoque[{}], receita[{}], chaves1, chaves2
# dict produto, fatura
# int tam

# pré: para i em {0..tam-1}: estoque[i]

# Passo 1. Leia a entrada e inicialize as variáveis
# Passo 1.1. Leia o tamanho do estoque
tam = int(input())

# Passo 1.2. Inicialize as abstrações
chaves1 = ['num', 'nome', 'qtde', 'custo', 'venda']  # chaves do dicionário
chaves2 = ['num', 'nome', 'lucro']  # chaves do dicionário
estoque = [dict.fromkeys(chaves1) for _ in
           range(tam)]  # lista de dicionários de produtos
receita = [dict.fromkeys(chaves2) for _ in range(tam)]  # lista de dicionários de faturas
produto = []  # lista para ler a entrada

# Passo 1.3. Leia o estoque
for i in range(tam):
    # Passo 1.3.1. Leia o produto
    produto = input().split()  # lido como lista de str
    estoque[i]['num'] = produto[0]
    estoque[i]['nome'] = produto[1]
    estoque[i]['tide'] = int(produto[2])  # converte para inteiro
    estoque[i]['custo'] = float(produto[3])  # converte para float
    estoque[i]['venda'] = float(produto[4])  # converte para float

# Passo 2. Calcule o provável lucro total
# Passo 2.1. Calcule o lucro de cada item
for i in range(tam):
    valor = (estoque[i]['venda'] - estoque[i]['custo']) * estoque[i]['qtde']

    # Passo 2.1.1. Copia parte do dicionário
    receita[i]['num'] = estoque[i]['num']
    receita[i]['nome'] = estoque[i]['nome']

    # Passo 2.1.2. Adiciona um campo no dicionário
    receita[i]['lucro'] = valor

# Passo 2.2. Calcule o lucro total
total = sum(receita[i]['lucro'] for i in range(tam))

# Passo 3. Imprime os resultados
print('{0:.2f}'.format(total))

# pós: para i em {0..tam-1}: receita[i] and
#      lucrototal == Soma i em {0..tam-1}: receita[i]['lucro']
# fim do módulo principal
