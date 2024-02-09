nome_programa = 'Conversor de medidas'
print(' {:20} '.format(nome_programa))
metros = int(input('Digite o valor em metros: '))
km = (10**(-3)) * metros
cm = (10**(2)) * metros
mm = (10**(3)) * metros


print('Em quilômetros = {}\n'
'Em centímetros = {}\n'
'Em milímetros = {}'
.format(km, cm, mm))
