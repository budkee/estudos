# Programador: Édson Cáceres
# Data: 20/08/2020
# Este programa utiliza o módulo PIL (pillow). O programa lê duas
# coordenadas (x1,y1) e (x2,y2) e gera e imprime uma reta entre os pontos
# Declaração dos módulos utilizados
from PIL import Image, ImageDraw
# início do módulo principal
# descrição das variáveis utilizadas
# Image imagem
# ImageDraw desenhe
# int largura, altura, x1, y1, x2, y2
# str padrao
# pré: x1 y1 x2 y2
# Passo 1. Defina o ambiente gráfico e leia os pontos
# Passo 1.1. Defina o tamanho da imagem
largura = 1200
altura = 800
# Passo 1.2. Defina o padrão de cores
padrao = 'RGB'
# Passo 1.3. Crie a imagem

imagem = Image.new(padrao, (largura,altura),color='white')
desenhe = ImageDraw.Draw(imagem)
# Passo 1.4 Leia duas coordenadas (x,y)
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
# Passo 2. Gere uma reta vermelha (x1,y1)-(x2,y2) na imagem
desenhe.line([(x1,y1),(x2,y2)],fill=(255,0,0))
# Passo 3. Mostre a reta na imagem
imagem.show()
# pós: uma reta (x1,y1)-9x2,y2) na imagem
# fim do módulo principal