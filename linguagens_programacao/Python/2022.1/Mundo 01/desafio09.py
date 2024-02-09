# Tabuada de um número

print('--------- Tabuada ---------\n')
num = int(input('Digite um número: \n'))
i = 0
print('A tabuada do número {} é: \n'.format(num))
while i < 10:
    i = i + 1
    r = num * i
    
    print('{} X {} : {}'.format(num, i, r))

print('\nFim.')
