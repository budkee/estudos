# Um inteiro positivo num é denominado um numero deficiente quando a soma de seus divisores próprios for menor que ele mesmo.
# Da mesma forma, um num será denomidado um número perfeito se a soma dos seus divisores próprios for igual a ele mesmo.
# Por fim, um num será denominado um numero abundante quando a soma dos seus divisores próprios for maior que ele mesmo.

# O programa a seguir faz a leitura de dois numeros (num1 e num2) inteiros representando o intervalo de interesse e retorna a classificação de todos os números entre eles.
# num % qualqerNum == 0 : é divisor desse num.

# Passo 1: Leia o intervalo
num1, num2 = map(int,input().split())

# Passo 2: Monte os loops
# Passo 2.1: Loop referente ao intervalo [num1,num2]
for i in range(num1, num2 + 1):
    div = []
    # Passo 2.1.1: Loop para retirar os divisores de cada número do intervalo
    for j in range(1, i):  # range(start, stop, step
        # Passo 2.1.1.1: construa a condicional para o termômetro
        if i % j == 0:
            # print(num, i)
            div.append(j) # Adicione na lista dos divisores
        else:
            pass
    #print(div)
    # Passo 2.1.2: Loop para somar os divisores da lista e criar o termometro
    soma = 0
    for num in div:
        soma += num
    #print(soma)
    # Passo 2.2: construa a condicional para classificar cada número do intervalo
    if soma < i:
        print('{} deficiente.'.format(i))
    elif soma == i:
        print('{} perfeito.'.format(i))
    elif soma > i:
        print('{} abundante.'.format(i))
    # Passo 3: imprima a saída adequada (i, msg)
