"""Este programa lê um conjunto de notas variando de 0.0 a 10.0, conta-as, armazena as notas numa lista e calcula a média aritmética das notas. A leitura de uma nota negativa indica o final da entrada. Após o cálculo da média, o programa computa o número de notas maiores que a média. O programa imprime o número de notas, a média das notas e o número de notas maiores que a média. """

# início do módulo principal

# descrição das variáveis utilizadas
# list  notas
# float nota, media
# int   num, mmedia

# pré: (nota[0]..nota[n]) and para i em {0..n-1}:
#       nota[i] >= 0.0 and  nota[i] <=10.0 and nota[n] < 0

# Passo 1. Leia uma nota e inicialize as variáveis
# Passo 1.1. Leia as notas e insira na lista
print('Entre com uma nota negativa para finalizar.')
nota = float(input('Nota: '))
# Passo 1.2. Inicialize a lista
notas = []
# Passo 1.3. Inicialize o número de notas
num = 0
# Passo 1.4. Enquanto a nota lida for maior que zero, repita
while nota >= 0.0:
    # Passo 1.4.1. Insira a nota na lista
    notas.append(nota)
# Passo 1.4.2. Conte a nota lida
    num += 1
# Passo 1.4.2. Leia a próxima nota
    nota = float(input('Nota: '))
# Passo 2. Calcule o número de notas maiores que a média
# Passo 2.1. Calcule a média das notas
# Passo 2.1.1.. Inicialize a variável soma das notas
soma = 0.0
# Passo 2.1.2. Calcule a soma das notas
for i in range(0, num):
    soma = soma + notas[i]
# Passo 2.1.3. Compute a média das notas
media = soma/num
# Passo 2.2. Calcule o número de notas maiores que a média
# Passo 2.2.1. Inicialize o número de notas maiores que a média
mmedia = 0
# Passo 2.2.2. Compute o número de notas maiores que a média
for i in range(0, num):
    if notas[i] > media:
        mmedia += 1
# Passo 3. Imprima os resultados
print('{0:d} notas com média = {1:3.1f}'.format(num, media))
print('{0:d} notas acima da média'.format(mmedia))

# pós: media == (Soma i em {0..n-1}:notas[i])/n and n > 0
#      and num == n and mmedia = Num i em {0..n-1}: notas[i]>media
# fim do módulo principal
