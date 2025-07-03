# Programa: somatoriafor08a.py
# Dados um inteiro n, calcular a soma dos n termos da
# sequência
# soma_{i=1}^{n} 2*i/(2*i-1)/2*i = 2/1 + 4/3 + 6/5 + 8/7 + ...
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
num = 2
den = 1
termo = num / den
# Passo 2.3. Repita n vezes
for i in range(2, n + 1):
    #   print(termo)
    # Passo 2.3.1. Adicione o termo
    soma = soma + termo
    # Passo 2.3.2. Calcule o próximo numerador
    num = 2 * i
    #   print(num)
    # Passo 2.3.3. Calcule o próximo denominador
    den = 2 * i - 1
    #   print(den)
    # Passo 2.3.4. Calcule o próximo termo
    termo = num / den
# Passo 3. Imprima o resultado
print('{0:.6f}'.format(soma))

# pós: soma == soma_{i=1}^{n} 2*i/(2*i-1)/2*i
# fim do módulo principal
