# Passo 1: leia o número de termos a serem calculados
num = int(input())
# Passo 2: calcule o resultado
# Passo 2.1: inicialize as variáveis soma, numerador, denominador e termo
soma = 0
numerador = 0
denominador = 1
termo = numerador/denominador
# Passo 2.2: monte o loop
for i in range(1, num+1):
    numerador = (i - 1)**3
    #print(numerador)
    denominador = i**2
    #print(denominador)
    termo = numerador / denominador
    #print(termo)
    soma += termo
    #print(soma)
# Passo 3: imprima o resultado
print('{:6f}'.format(soma))