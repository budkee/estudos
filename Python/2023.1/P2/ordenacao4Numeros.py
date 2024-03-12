# Programa: ordena01.py
# Programador:
# Data: 15/09/2016
# Este programa lê um conjunto de quatro números, e usando o método bolha
# de ordenação, ordena os números em ordem não decrescente e imprime
# o conjunto de números ordenado
# início do módulo principal
# descrição das variáveis utilizadas
# float num1, num2, num3, num4
# bool trocou

# pré: num1 num2 num3 num4

# Passo 1. Leia a entrada e inicialize as variáveis
# Passo 1.1. Leia um conjunto com quatro números reais
print('Leia o conjunto de números: ')
num1, num2, num3, num4 = map(float, input().split())
# Passo 1.2. Inicialize o conjunto como não ordenado
trocou = True
# Passo 2. Enquanto o conjunto não estiver ordenado, repita
while trocou:
    # Passo 2.1. Suponha que o conjunto não está ordenado
    trocou = False
    # Passo 2.2. Mova o menor elemento para num1 e o maior para num2
    if num1 > num2:
        num1, num2 = num2, num1  # troque num1 com num2
        trocou = True  # troca efetuada
    # Passo 2.3. Mova o menor elemento para num2 e o maior para num3
    if num2 > num3:
        num2, num3 = num3, num2  # troque num2 com num3
        trocou = True  # troca efetuada
    # Passo 2.4. Mova o menor elemento para num3 e o maior para num4
    if num3 > num4:
        num3, num4 = num4, num3  # troque num3 com num4
        trocou = True  # troca efetuada
# se trocou == True é porque houve troca e o conjunto não estava ordenado
# Passo 3. Imprima o conjunto de números ordenado
print('{0:4.1f} {1:4.1f} {2:4.1f} {3:4.1f}'.format(num1, num2, num3, num4))

# pós: para i = {1, 2, 3}:num_i <= num_(i+1)
# fim do módulo principal
