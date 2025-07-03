# Programa: nomes00.py
# Programador:
# Data:

# Este programa lê um registro com o número, nome, as 3 notas das
# provas e as 2 notas de trabalho da disciplina de AlgProg I. A
# média das provas é dada por MP = (P1+P2+P3)/3.0, a média dos
# trabalhos por MT = (T1 + T2)/2.0 e a média final por
# MF = 0.75*MP + 0.25*MT. O programa computa a média final e
# imprime o número, nome e a média final de cada aluno.

# início do módulo principal
# descrição das variáveis e estruturas utilizadas
# list chaves[], dados[]
# dict estudante{}
# float mediaprovas, mediatrabalhos, mediafinal
# int tam

# pré: para i em {0..tam-1}: numero, nome, notas[0] notas[1] notas[2]
#      notas[3] notas[4]

# Passo 1. Leia o entrada e inicialize as variáveis
# Passo 1.1. Leia o número de alunos
tam = int(input())
# Passo 1.2. Inicialize as variáveis
chaves = ['numero','nome','notas'] # chaves do dicionários
estudante = dict.fromkeys(chaves)
dados = [] # lista de strings para ler a entrada
# Passo 1.3. Leia os dados dos alunos
for i in range(tam):
   dados = input().split(', ') # lido como lista de strings
   estudante['numero'] = int(dados[0]) # converta para inteiros
   estudante['nome'] = dados[1]
   estudante['notas'] = list(map(float,dados[2].split())) # lista floats
# Passo 1.3.2. Calcule a média final do aluno
# Passo 1.3.2.1. Calcule a média das provas
   mediaprovas = sum(estudante['notas'][:3])/3.0
# Passo 1.3.2.2. Calcule a média dos trabalhos
   mediatrab = sum(estudante['notas'][3:])/2.0
# Passo 1.3.2.3. Calcule a média final
   mediafinal = 0.75*mediaprovas + 0.25*mediatrab
# Passo 1.3.2.4. Imprime os resultados
print(estudante)
#for i in range(tam):
 #  print('{0:d}  '.format(estudante['numero']), end='')
  # print('{0:s} {1:.1f}'.format(estudante['nome'], mediafinal))

# pós: para i em {0..tam-1}: nome, mediafinal[i] and
#      mediafinal[i] == 0.75*mediaprovas[i]+0.25*mediatrabalhos[i]
#      and mediaprovas[i] ==(notas[0] + notas[1] + notas[2])/3.0
#      and mediatrabalhos[i] == (notas[3] + notas[4])/2.0
# fim do módulo principal
