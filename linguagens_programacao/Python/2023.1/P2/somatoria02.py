# Programa: somatoria02.py
# Programador:
# Data: 27/05/2016
# Este programa lê um valor de n e computa a soma dos n
# primeiros termos da sequência
# 100/0! + 99/1! + 98/2! + 97/3! + ... ,
# e imprime o resultado.
# início da função principal
# descrição das variáveis utilizadas
# int num, numerador, denominador
# float termo, soma

# pré: num
# Passo 1. Leia o valor de num e inicialize somatória
# Passo 1.1. Leia o valor de num
num = int(input())
# Passo 1.2. Inicialize o valor de soma com 0.0
soma = 0.0
# Passo 2. Calcule a soma dos n primeiros termos
# Passo 2.1. Compute o primeiro termo
# Passo 2.1.1. Compute o primeiro numerador
numerador = 100
# Passo 2.1.2. Compute primeiro denominador
denominador = 1 # 0!
# Passo 2.1.3. Compute primeiro termo
termo = numerador/denominador
# Passo 2.2. Para i em [1,num] some os i-ésimos termos
for i in range(1,num+1):
# Passo 2.2.1. Some o i-ésimo termo
    soma = soma + termo
# Passo 2.2.2. Compute i+1-ésimo numerador
    numerador = 100 - i
# Passo 2.2.3. Compute i+1-ésimo denominador
    denominador = denominador*i
# Passo 2.2.4. Compute i+1-ésimo termo
    termo = numerador/denominador
# Passo 3. Imprima o valor da soma da sequência
print('Soma: {0:f}'.format(soma))

# pós: soma == Soma i em {0,...,num-1}:termo[i] and
#      termo[i] == (100-i)/(i!)
# fim da função principal