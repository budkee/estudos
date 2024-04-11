a, b, c, d, e = input('Insira 5 números: ').split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

maior = -1
menor = 10
for s in [a,b,c,d,e]:

    if s > maior:
        maior = s

    if s < menor:
        menor = s


print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))