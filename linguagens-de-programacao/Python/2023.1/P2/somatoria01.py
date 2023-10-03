# Algoritmo: Somatoria01

# Passo 1. Leia o valor de num e inicialize somatória
# Passo 1.1. Leia o valor de num
num = int(input())
# Passo 1.2. Inicialize o valor de soma com 0.0
soma = 0
# Passo 2. Calcule a soma dos n primeiros termos
# Passo 2.1. Compute o primeiro termo
# Passo 2.1.1. Compute o primeiro numerador
numerador = 100
# Passo 2.1.2. Compute primeiro denominador
denominador = 1
# Passo 2.1.3. Compute primeiro termo
termo = numerador/denominador
# Passo 2.2. Para i em [1,num] some os i-ésimos termos
for i in range(1, num+1):
# Passo 2.2.1. Some o i-ésimo termo
    soma += termo
# Passo 2.2.2. Compute i+1-ésimo numerador
    numerador = 100 - i
# Passo 2.2.3. Compute i+1-ésimo denominador
    denominador = 2**i
# Passo 2.2.4. Compute i+1-ésimo termo
    termo = numerador/denominador
# Passo 3. Imprima o valor da soma da sequência
print(soma)
# fim do algoritmo