# Programa: somatoriafor03.py
# Dados os inteiros a e b, calcular e imprimir a 
# soma dos números ímpares maiores ou iguais que a e
# menores ou iguais que b
# início do módulo principal
# descrição das variáveis utilizadas
# int a, b, soma

# pré: a,b

# Passo 1. Leia a entrada
a, b = map(int, input().split())
# Passo 2. Calcule a soma dos números ímpares entre a e b
# Passo 2.1. Inicialize a soma
soma = 0
# Passo 2.2. Para i em [a,b] faça
for i in range(a, b + 1):
    print(i)
    # Passo 2.2.1. Verifique se o número é ímpar
    if i % 2 != 0:
        # Passo 2.2.1.1. Adicione i a soma
        soma += i  # soma = soma + i
        print('somei')
# Passo 3. Imprima o resultado
print(soma)

# pós: soma == Soma i em {a+1..b}:i | i%2 != 0
# fim do módulo principal
