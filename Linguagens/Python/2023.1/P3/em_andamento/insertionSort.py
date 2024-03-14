# Função para ordenar por inserção usando dicionário
tam = int(input('Insira o tamanho da lista de dados: '))
chaves = input('Quais vão ser as chaves do seu dicionário? Separe com ,: '
                       '').split(',')
# Inicialize a lista e o dicionário
dicionario = dict.fromkeys(chaves)
dados = []

print(chaves)
# print(dicionario): tudo certo até aqui.

# Receba a entrada
for i in range(tam):
    dados = input('Entre com um novo dado: ').split()
    dicionario[chaves[0]] = dados[0]
    dicionario[chaves[1]] = dados[i]

print(dicionario)