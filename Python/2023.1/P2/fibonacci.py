# Passo 1: leia o número representando a quantidade de termos a serem somados na sequência
n = int(input())
# Passo 2: calcule o resultado
# Passo 2.1: inicialize as variáveis soma, numerador, denominador e termo
numA = 0
numB = 1
i = 0
# Passo 2.2: monte o loop
while i < n:
    num = numA + numB
    numB = numA
    numA = num
    # Passo 3: imprima o resultado
    print('{}'.format(num), end=' ')
    i += 1

