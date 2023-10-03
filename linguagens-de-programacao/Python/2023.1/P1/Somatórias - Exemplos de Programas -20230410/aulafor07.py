# Programa: somatoriafor07.py
# Dados os inteiros a e b, calcular e imprimir os 
# quadrados dos números menores ao maior
# ou maiores ou iguais ao menor (ordem inversa).
# Ex. 2 9
# 81 64 49 36 25 16 9 4
# início do módulo principal
# descrição das variáveis utilizadas
# int a, b, maior, menor, quadrado
# str msg

# pré: a,b

# Passo 1. Leia a entrada
a, b = map(int, input().split())
# Passo 2. Compute e imprima os quadrados na ordem inversa
# Passo 2.1. Compute o maior e o menor
if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
# Passo 2.2. Inicialise a mensagem
msg = ''
# Passo 2.3. Para i em [maior,menor] faça
for i in range(maior - 1, menor - 1, -1):
    print(i)
    # Passo 2.3.1. Compute o quadrado de i
    quadrado = i * i
    # Passo 2.3.2.
    msg = msg + '{} '.format(quadrado)
    print('concatenei')
# Passo 3. Imprima o resultado
print(msg)

# pós: para i em {maior..menor}:i*i
# fim do módulo principal
