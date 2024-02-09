# Programa: somatoriafor05.py
# Dados os inteiros a e b, calcular e imprimir a 
# soma dos números ímpares maiores ou iguais que a e
# menores ou iguais que b
# início do módulo principal
# descrição das variáveis utilizadas
# int a, b, soma

# pré: a,b

# Passo 1. Leia a entrada
a, b = map(int, input().split())
# Passo 2. Calcule a soma
# Passo 2.1. Inicialize a soma
soma = 0
# Passo 2.2. Verifique se o a é ímpar
if a % 2 == 0:
    a = a + 1
# Passo 2.2. Para i%2 != 0 em [a,b] faça
for i in range(a, b + 1, 2):
    print(i)
    # Passo 2.3.1. Adicione i a soma
    soma += i  # soma = soma + i
    print('somei')
# Passo 3. Imprima o resultado
print(soma)

# pós: soma == Soma i em {a..b}:i | i%2 != 0
# fim do módulo principal
