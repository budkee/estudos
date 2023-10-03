# Programa: equacao2grau.py
# Programador:
# Data: 01/09/2016
# Este algoritmo lê três coeficientes, a, b e c de uma equação do segundo
# grau (ax^2 + bx + c = 0), e utilizando a fórmula de Báscara calcula (se
# existirem) as raízes da equação ou imprime uma mensagem caso contrário
# declaração das bibliotecas utilizadas
import math
# início do módulo principal
# descrição das variáveis utilizadas
# float a, b, c, delta, r1, r2
# pré: a b c and a != 0
# Passo 1. Leia os coeficientes da equação
print('Entre com os três coeficientes: ')
a, b, c = map(float,input().split())
# Passo 2. Calcule as raízes reais
# Passo 2.1. Calcule o valor de delta
delta = b*b - 4*a*c
# Passo 2.2. Compute a msg sobre as raízes
if delta >= 0: # possui raízes
   r1 = (-b - math.sqrt(delta))/(2*a)
   r2 = (-b + math.sqrt(delta))/(2*a)
   msg = 'r1 = {0:f}, r2 = {1:f}'.format(r1, r2)
else: # não possui raízes
   msg = 'Não possui raízes reais.'
# Passo 3. Imprima as raízes ou a mensagem adequada
print(msg)
# pós: (para i em {1,2}, r[i] ==(-b +- sqrt(delta))/(2*a) and
#      delta >=0 and delta == b*b-4*a*c or
#      msg == 'Não possui raízes reais.'
# fim do módulo principal