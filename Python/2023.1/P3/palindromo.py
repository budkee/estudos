palavra = str(input())

inversa = ''

for letra in palavra:
    inversa = letra + inversa
if inversa == palavra:
    print('palíndromo')
else:
    print('não palíndromo')
