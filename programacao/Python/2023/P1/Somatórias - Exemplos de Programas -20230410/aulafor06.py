# Programa: somatoriafor06.py
# Dados os inteiros a e b, calcular e imprimir a 
# soma dos números maiores ou iguais que o menor e
# menores ou iguais que o maior
# início do módulo principal
# descrição das variáveis utilizadas
# int a, b, maior, menor, soma

# pré: a,b

# Passo 1. Leia a entrada
a, b = map(int, input().split())
# Passo 2. Calcule a soma de i em [menor,maior]
# Passo 2.1. Compute o maior e o menor
if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
# Passo 2.2. Inicialize a soma
soma = 0
# Passo 2.3. Para i em [menor,maior] faça
for i in range(menor, maior):
    print(i)
    # Passo 2.3.1. Adicione i a soma
    soma += i  # soma = soma + i
    print('somei')
# Passo 3. Imprima o resultado
print(soma)

# pós: soma == Soma i em {menor..maior}:i 
# fim do módulo principal
