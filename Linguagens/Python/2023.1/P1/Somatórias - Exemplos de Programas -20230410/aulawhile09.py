# Programa: somatoriawhile09.py
# Dados um inteiro n, calcular a soma dos n termos da
# sequência
# soma_{i=0}^{n-1} i**2/i! = 0 + 1 + 4/2 + 9/6 + 16/24 +....
# início do módulo principal
# descrição das variáveis utilizadas
# int n, soma, num, den, termo

# pré: n

# Passo 1. Leia a entrada
n = int(input())
# Passo 2. Calcule a soma dos n termos da sequência
# Passo 2.1. Inicialize a soma
soma = 0.0
# Passo 2.2. Compute o primeiro termo
num = 0
den = 1
termo = num / den
# Passo 2.3. Inicialize o número de termos
i = 1
# Passo 2.4. Repita n vezes
while i <= n:
    print(termo)
    # Passo 2.4.1. Adicione o termo
    soma = soma + termo
    # Passo 2.4.2. Calcule o próximo numerador
    num = i ** 2
    print(num)
    # Passo 2.4.3. Calcule o próximo denominador
    den = den * i
    print(den)
    # Passo 2.4.4. Calcule o próximo termo
    termo = num / den
    # Passo 2.4.5. Incremente o número de termos
    i += 1
# Passo 3. Imprima o resultado
print(soma)

# pós: soma == soma_{i=0}^{n-1} i**2/i!
# fim do módulo principal
