# -*- coding: utf-8 -*-
# Programa: triangulo.py
# Programador:
# Data: 12/10/2015
# Este programa lê três números reais e verifica se eles
# podem ser os comprimentos dos lados de um triângulo e se forem,
# verificar se é um triângulo equilátero, isósceles ou escaleno. Se não
# formarem um triangulo, escrevem uma mensagem.
# início do módulo principal
# descrição das variáveis utilizadas
# float lado1, lado2, lado3
# bool triângulo
# str msg

# pré: lado1 lado2 lado3

# Passo 1. Leia os lados
#print('Leia três numeros reais (lados): ')
lado1 = float(input())
lado2 = float(input())
lado3 = float(input())
# Passo 2. Verifique se formam um triangulo e classifique
a = lado1 > abs(lado2 - lado3) and lado1 < lado2 + lado3
b = lado2 > abs(lado1 - lado3) and lado2 < lado1 + lado3
c = lado3 > abs(lado2 - lado1) and lado3 < lado2 + lado1
triangulo = a and b and c
if triangulo:
# Passo 2.1. Classifique o tipo de triângulo
    if (lado2 == lado1) and (lado3 == lado1):
        msg ='equilátero'
    elif (lado2 == lado1) or (lado2 == lado3) or (lado3 == lado1):
        msg = 'isósceles'
    else:
        msg = 'escaleno'
# Passo 2.2. Imprima a mensagem que não é triângulo
else:
    msg = 'não é triangulo'
# Passo 3. Imprima a classificacao
print('lados: {0:.2f}, {1:.2f}, {2:.2f} - {3:s}'.format(lado1, lado2, lado3, msg))

# pós: (triangulo == (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2)}
#      and (lado2 + lado3 > lado1)) and (("nao e triangulo" and}
#      triangulo == false) or "equilatero" or "isosceles" or "escaleno")}
# fim do módulo principal

