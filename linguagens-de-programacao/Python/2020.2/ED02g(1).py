import math
print('Determinar as raízes de uma equação do 2º grau\n'
      'Tendo y = ax² + bx + c')
a = float(input('Coeficiente a: '))
b = float(input('Coeficiente b: '))
c = float(input('Coeficiente c: '))

r1 = (- b + math.sqrt(b*b - 4 * a * c))/2 * a
r2 = (- b - math.sqrt(b*b - 4 * a * c))/2 * a

print('As raízes da equação são {} e {}'.format(r1, r2))
