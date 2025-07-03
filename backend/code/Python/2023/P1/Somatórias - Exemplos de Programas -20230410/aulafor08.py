# Programa: somatoriafor08.py
# Dados um inteiro n, calcular a soma dos n termos da
# sequência
# soma_{i=1}^{n} (2*i-1)/2*i = 1/2 + 3/4 + 5/6 + 7/8 + ...
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
num = 1
den = 2
termo = num/den
# Passo 2.3. Repita n vezes
for i in range(1,n+1):
   print(termo)
# Passo 2.3.1. Adicione o termo
   soma = soma + termo
# Passo 2.3.2. Calcule o próximo numerador
   num = 2*(i+1) - 1
   print(num)
# Passo 2.3.3. Calcule o próximo denominador
   den = 2*(i+1)
   print(den)
# Passo 2.3.4. Calcule o próximo termo
   termo = num/den
# Passo 3. Imprima o resultado
print(soma)

# pós: soma == soma_{i=1}^{n} (2*i-1)/2*i
# fim do módulo principal
