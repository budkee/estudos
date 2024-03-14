# Programa dicionarios05Notas.py
# Programador: budkee
# Data: 21/06/23

# A avaliação da disciplina de Algoritmos e Programação I
# é composta de três provas e dois trabalhos. Projete um
# programa que leia um conjunto de alunos com as respectivas notas
# das provas e dos trabalhos. O programa deve ordenar os alunos pelo
# primeiro nome usando o método de ordenação por inserção
# (insertionSort). O programa deve imprimir a lista dos alunos ordenada
# pelo primeiro nome.

# início do módulo principal


# Passo 1. Leia a entrada
# Passo 1.1. Leia o tamanho do conjunto de conjunto de teste
tam = int(input())
# Inicialize as estruturas
chaves = ['nome', 'sobrenome', 'notas']
estudantes = [dict.fromkeys(chaves) for _ in range(tam)]
# print(estudantes)
dados = [str, str, [0.0] * 5]

# Passo 1.2. Leia os dados dos estudantes
for i in range(tam):
    # Leitura
    dados = input().split(',')  # Com a divisão feita pela vírgula,
    # dá pra reconhecer a lista de notas na linha 36.

    # Atribuição
    estudantes[i]['nome'] = dados[0]
    estudantes[i]['sobrenome'] = dados[1]
    estudantes[i]['notas'] = list(map(float, dados[2::]))

    # Média final do aluno
    # 1. Media provas
    mediaprovas = sum(estudantes[i]['notas'][:3]) / 3.0
    # 2. Media trabalho
    mediatrab = sum(estudantes[i]['notas'][3:]) / 2.0
    # 3. Media final
    estudantes[i]['mf'] = round(0.75 * mediaprovas + 0.25 * mediatrab, 1)

# print(estudantes): tudo certo até aqui.

# Passo 2.2 Ordene os dados pelo ordem alfabética
trocou = True
while trocou:
    trocou = False
    for i in range(0, tam-1):
        if estudantes[i]['nome'] > estudantes[i+1]['nome']:
            estudantes[i], estudantes[i+1] = estudantes[i+1], estudantes[i]
            trocou = True

# print(estudantes): tudo certo até aqui.

# Passo 3. Imprima os Dados
for i in range(tam):
    print('{0:s} {1:s} {2:.1f}'.format(estudantes[i]['nome'], estudantes[i]['sobrenome'],
                                       estudantes[i]['mf']))

# fim do módulo principal
