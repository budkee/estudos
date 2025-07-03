# Programador: Edson
# Data: 21/08/2020
# Este programa utiliza o módulo turtle.
# O programa lê dois pontos (x,y) e gera e imprime uma reta
# entre os dois pontos.
# Declaração dos módulos utilizadas
from turtle import *
# início do módulo principal
# descrição das variáveis utilizadas
# float x1, y1, x2, y2
# pré: x, y
# Passo 1. Leia a entrada e defina a as variáveis
# Passo 1.1. Leia duas coordenadas(x,y)
x1, y1 = map(float,input().split())
x2, y2 = map(float,input().split())
# Passo 1.2. Defina a cor
colormode(255) # escala [0,255]
pencolor(255,0,0) # cor vermelha
# Passo 2. Gere e imprima a reta entre os dois pontos
# Passo 2.1. Apague a tartaruga
hideturtle()
# Passo 2.2. Levante a caneta
penup()
# Passo 2.3. Vá para a posição inicial
setpos(x1,y1)
# Passo 2.4. Abaixe a caneta
pendown()
# Passo 2.3. Vá para a posição final
setpos(x2,y2)
# pós: uma reta vermelha ligando dois pontos
# fim do módulo principal