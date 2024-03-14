print('\nTipos primitivos\n')
objeto = input('Digite algo: \n')

print('O objeto é numérico? -> {}'.format(objeto.isnumeric()))
print('O objeto é uma String? -> {}'.format(objeto.isalpha()))
print('O objeto é alpha-numérico? -> {}'.format(objeto.isalnum()))
print('O objeto está em minúsculo? -> {}'.format(objeto.islower()))
print('O objeto está em MAIÚSCULO? -> {}'.format(objeto.isupper()))

print('Tipo primitivo do objeto -> {} \n'.format(type(objeto)))
