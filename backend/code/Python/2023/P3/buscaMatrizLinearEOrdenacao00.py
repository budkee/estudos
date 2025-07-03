# Método de busca: linear
# Programa:
# Programador:
# Data:

# Este programa lê um conjunto de tam nomes e telefones de uma
# empresa telefônica. Os nomes são dados pelo nome, sobrenome
# e número de telefone. O programa elabora uma lista telefônica
# ordenando o conjunto pelo sobrenome. Os dados são armazenados
# em uma lista, onde cada elemento é uma lista, com três strings,
# nomes, sobrenomes e numeros.

# início do módulo principal.

# descrição das variáveis utilizadas
# list catalogo[[]]
# int tam

# pré: tam catalogo[0] catalogo[1] .. catalogo[tam-1]

# Passo 1. Leia a entrada e inicialize as variáveis
# Passo 1.1. Leia o tamanho do catálogo
tam = int(input())
# Passo 1.2. Inicialize as listas
catalogo = [[''] * 3 for i in range(tam)]
# Passo 1.3. Leia os dados dos assinantes
for i in range(tam):
    catalogo[i] = list(map(str, input().split()))
# Passo 2. Ordene pelo sobrenome dos assinantes
# Passo 2.1. Assuma que houve troca
trocou = True
# Passo 2.2. Compare os termos dois a dois, trocando quando necessário
while trocou:
    # Passo 2.2.1. No início da iteração não houve troca
    trocou = False
    for i in range(0, tam - 1):
        if catalogo[i][1] > catalogo[i + 1][1]:
            catalogo[i], catalogo[i + 1] = catalogo[i + 1], catalogo[i]
            trocou = True
# Passo 3. Imprima o catálogo
for i in range(0, tam):
    print('{0:s} {1:s} {2:s}'.format(catalogo[i][1], catalogo[i][0], catalogo[i][2]))

# pós: para i em {0..tam-1}:catalogo[i] and
#      catalogo[i][1] <= catalogo[i+1][1]
# fim do módulo principal
