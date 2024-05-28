import math
def r(x):
    r = (((v0)**2) * 1) / 9.81
    return r
def hmax(x):
    h = ((v0 ** 2) * 0.5 )/ 19.62
    return h

v0 = int(input('Qual a Velocidade Inicial(m/s) do projétil? '))

print('O alcance máximo (em um ângulo de 45º) foi de {:.2f} metros de distância e a altura máxima foi de {:.2f} metros.'.format(r(v0), hmax(v0)))


