# Passo 1: leia o número representando a quantidade de termos a serem somados na sequência
num = int(input())
# Passo 2: calcule o resultado
# Passo 2.1: inicialize as variáveis soma, numerador, denominador e termo
soma = 0
numerador = 1
denominador = 1
termo = numerador/denominador
# Passo 2.2: monte o loop
if num <= 50:
    for i in range(1, num+1):
        numerador = 2*i - 1
        #print(numerador)
        denominador = i
        #print(denominador)
        termo = numerador / denominador
        #print(termo)
        soma += termo
        #print(soma)
else:
    exit()
# Passo 3: imprima o resultado
print('Soma: {:6f}'.format(soma))