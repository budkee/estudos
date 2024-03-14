print('Algoritmo para calcular e escrever o valor de s.')
S = 1
for n in range(1,101):
    S += 1/n
print('%.2f' % S)
#    print('n = %.2f -> s = %.2f' % (n,S))
