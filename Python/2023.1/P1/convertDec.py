# Passo 1: leia a entrada
binario = int(input('Entre com um número binário de até 3 dígitos: '))
# Passo 2: Converta o número para a base 10.
decimal = 0
aux = binario
digito = aux % 10 # obtenha o dígito menos significativo (dígito mais a direita)
aux = aux // 10 # retire o dígito menos significativo.
decimal = decimal + digito*2**0
digito = aux % 10
aux = aux // 10
decimal = decimal + digito*2**1
digito = aux % 10
aux = aux // 10
decimal = decimal + digito*2**2
# Passo 3: imprima o resultado
print('{0:d} (base 2) == {1:d} (base 10)'.format(binario, decimal))