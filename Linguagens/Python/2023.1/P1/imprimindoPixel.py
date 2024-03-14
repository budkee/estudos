# Este programa utiliza o módulo pillow (PIL).
# Ele gera e imprime um pixel na tela.
# Declaração dos módulos utilizadas
from PIL import Image
# início do módulo principal
# descrição das variáveis utilizadas
# int x, y
# pré: x y
# Passo 1. Defina o tamanho da imagem e leia o ponto
# Passo 1.1. Defina o tamanho da imagem
largura = 1200
altura = 800
# Passo 1.2. Defina o padrão de cores
padrao = 'RGB'
# Passo 1.3. Cria uma nova imagem com fundo branco.
imagem = Image.new(padrao, (largura,altura), color='brown')
# Passo 1.4 Leia um ponto (x,y)
x = int(input())
y = int(input())
# Passo 2. Gere o pixel vermelho de coordenadas (x,y) na imagem
imagem.putpixel((x,y),(255,0,0))
# Passo 3. Mostre a imagem resultante
imagem.show()
# pós: um pixel vermelho na tela
# fim do módulo principal