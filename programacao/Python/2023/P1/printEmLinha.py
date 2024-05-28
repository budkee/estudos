# Passo 1: leia os números
num1, num2 = map(int, input().split())
# Passo 2: Compute a saída
# Passo 2.1: Compute o maior e o menor número
menor = min(num1, num2)
maior = max(num1, num2)
# Passo 2.2: Implemente o loop dos números ímpares
for num in range(menor, maior + 1):
    if num % 2 != 0:
        result = num ** 2
        # Passo 3: Imprima o resultado em uma só linha
        print('{0:1d}'.format(result), end=' ')