# Programa para inclusão e busca de livros em uma biblioteca

# A entrada é dada em duas partes:
# 1. Quantidade de livros a serem incluídos, seguido do nome do livro, autor e
# localização na prateleira.
# 2. Quantidade de buscas, seguido dos nomes dos livros a serem buscados

# A saída é dada pelo nome do autor do livro e o número da prateleira onde se encontra,
# caso exista no acervo.
# Caso não exista, retorne com a mensagem ''nome do livro' não encontrado'.

# Início do módulo principal

# Parte 1: Entrada de livros
# Leia a quantidade de livros
num = int(input())
# Inicialize as chaves, o dicionário e a lista dos dados
chaves = ['nome do livro', 'autor', 'prateleira']
livros = [dict.fromkeys(chaves) for _ in range(num)]
dados = []
# Leia os livros
for i in range(num):
    dados = input().split(', ')
    livros[i]['nome do livro'] = dados[0]
    livros[i]['autor'] = dados[1]
    livros[i]['prateleira'] = int(dados[2])

# print(livros): tudo certo até aqui

# Parte 2: Busca por livros
# Leia a quantidade de buscas
buscas = int(input())
# Leia o nome dos livros de interesse
for j in range(buscas):

    livro = input()

    # Busca
    encontrou = False
    i = 0
    pos = 0
    while i < num and not encontrou:
        if livros[i]['nome do livro'] == livro:
            pos = i
            encontrou = True
        i += 1
    if encontrou:
        autor = str(livros[pos]['autor'])
        prateleira = str(livros[pos]['prateleira'])
        msg = autor + ' ' + prateleira

    else:
        msg = livro + ' não encontrado'

    # Imprima o resultado da busca
    print(msg)

# Fim do módulo principal