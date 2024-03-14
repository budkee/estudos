# Leia o tamanho do catálogo
tam = int(input())
# Inicialize as estruturas
chaves = ['sobrenome', 'nome', 'telefone']
catalogo = [dict.fromkeys(chaves) for _ in range(tam)]
dados = []
# Leia a linha i do catálogo
for i in range(tam):
    dados = input().split(', ')
    catalogo[i]['sobrenome'] = dados[0]
    catalogo[i]['nome'] = dados[1]
    catalogo[i]['telefone'] = dados[2]

# Leia o número de buscas
num = int(input())
# Leia as buscas
for j in range(num):
    nome, sobrenome = input().split()

    # Faça a busca
    encontrou = False
    i = 0
    pos = 0
    while i < tam and not encontrou:
        if catalogo[i]['sobrenome'] == sobrenome and catalogo[i]['nome'] == nome:
            pos = i     # Declara a posição do match
            encontrou = True
        i += 1
    if encontrou:
        msg = catalogo[pos]['telefone']
    else:
        msg = 'não tem telefone'

    # Imprima o resultado da busca
    print('{0:s} {1:s} {2:s}'.format(nome, sobrenome, msg))
