# Programa notas00.py
# Programador: budkee
# Data: 23/06/2023

# A avaliação da disciplina de Algoritmos e Programação I
# é composta de três provas e dois trabalhos. Projete um
# programa que leia um conjunto de alunos com as respectivas notas
# das provas e dos trabalhos. O programa deve ordenar os alunos pelo
# primeiro nome usando o método de ordenação por inserção
# (insertionSort). O programa deve imprimir a lista dos alunos ordenada
# pelo primeiro nome.
# início do módulo principal

# Variáveis
# número de alunos: n - int
# conjunto de alunos: estudante - dicionario
# nome dos alunos: nome - string
# sobrenome do aluno: snome - string
# notas dos alunos: notas - float

# Funções
# ordenar os alunos em ordem alfabética pelo primeiro nome: ordena(dados - lista)
def ordenaInsert(lista):
    print(lista)
    # Leia o tamanho da lista
    tam = len(lista)
    # Ordenação
    for i in range(1, tam):
        temp = lista[i]
        del lista[i]
        # Percorra a lista pelo final
        j = i - 1
        # Enquanto o percurso for menor ou igual a 0 e a temporária for menor que o
        # elemento j da lista, faça:
        while j <= 0 and temp < lista[j]:
            # Retorne com o índice pela esquerda.
            j -= 1
        # Insira a temporária na posição de j
        lista.insert(j + 1, temp)

    return lista


# calcula a média: media()

def media(lista):

    # Média dos Trabalhos
    mt = sum(lista[3::]) / 2
    # Média das Provas
    mp = sum(lista[0:3]) / 3
    # Média Final
    valor = 0.75 * mp + 0.25 * mt

    return valor


# Passo 1. Leia a entrada
# Passo 1.1. Leia o tamanho do conjunto de conjunto de teste
n = int(input())
# Passo 1.2. Leia os dados dos estudantes
chaves = ['nome', 'snome', 'notas', 'mf']
estudante = dict.fromkeys(chaves)
dados = []
# Passo 2. Ordene os dados
for i in range(n):
    dados = input().split()
    estudante['nome'] = dados[0]
    estudante['snome'] = dados[1]
    estudante['notas'] = list(map(float, dados[2].split()))


    # Calcule a média
    # Média dos Trabalhos
    mt = sum(estudante['notas'][3::]) / 2
    # Média das Provas
    mp = sum(estudante['notas'][0:3]) / 3
    # Média Final
    mf = 0.75 * mp + 0.25 * mt

    #estudante['mf'] = mf

print(estudante['nome'])

# Ordene a lista pelo nome
#for i in range(1, n):
    #temp = estudante[i]

# Imprima o resultado
#for i in range(n):
    #print('{0:s} {1:s} {2:.1f}'.format(estudante[i]['nome'], estudante[i]['snome'],
                               #estudante[i]['mf']))

# fim do módulo principal
