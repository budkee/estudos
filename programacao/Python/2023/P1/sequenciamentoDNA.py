# Tandem repeats: busca pelo maior número de repetições de cada uma das substrings
# Este programa lê uma string e três substrings, calcula e
# imprime o número de vezes que cada substring aparece na string.
# inicio do módulo principal
# descrição das variáveis locais utilizadas
# string sequencia, subseq1, subseq2, subseq3
# int numsubseq1, numsubseq2, numsubseq3
# pré: sequencia subseq1 subseq2 subseq3
# Passo 1. Leia uma sequência e 3 subsequências
# Passo 1.1. Leia uma sequência
sequencia = input('Leia uma sequência de DNA: ')
# Passo 1.2. Leia a subsequência 1
subseq1 = input('Leia a subsequência 1: ')
# Passo 1.3 Leia a subsequência 2
subseq2 = input('Leia a subsequência 2: ')
# Passo 1.4. Leia a subsequência 3
subseq3 = input('Leia a subsequência 3: ')
# Passo 2. Calcule o número de vezes que a subseq aparece
numsubseq1 = sequencia.count(subseq1)
numsubseq2 = sequencia.count(subseq2)
numsubseq3 = sequencia.count(subseq3)
# Passo 3. Imprima o num de vezes que cada subseq aparece
print('{0:s} - {1:d}'.format(subseq1,numsubseq1))
print('{0:s} - {1:d}'.format(subseq2,numsubseq2))
print('{0:s} - {1:d}'.format(subseq3,numsubseq3))