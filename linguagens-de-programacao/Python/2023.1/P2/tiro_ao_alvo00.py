# Programa: tiroaoalvo01.py
# Programador:
# Data: 23/02/2018
# Este programa utiliza as bibliotecas pygame e playsound.
# O programa gera um alvo e lendo os movimentos do mouse e
# o clique do botão esquerdo simula o lançamento de um dardo
# na região gráfica. Se o botão esquerdo do mouse for
# pressionado dentro do círculo, um ponto é marcado e um som
# é reproduzido. Se o o botão esquerdo for pressionado fora
# do círculo, um ponto é impresso, mas sem nenhum som. Para
# finalizar o jogo, basta pressionar o botão direito do mouse.
# declaração das bibliotecas utilizadas
import pygame # >= v.2.0
import playsound
# início do módulo principal
# descrição das variáveis utilizadas
# bool atira
# str cor, text
# mouse botoes, x, y
# font fonte
# display tela

# pré: x, y posição do mouse na tela em cada jogada

# Passo 1. Defina o ambiente gráfico
# Passo 1.1. Defina o tamanho da imagem/tela
largura = 640
altura = 480
# Passo 1.2. Inicialize o pygame
pygame.init()
# Passo 1.3. Crie a janela gráfica (tela)
tela = pygame.display.set_mode((largura, altura))
# Passo 1.4. Defina a cor do fundo da janela
tela.fill('white')
# Passo 1.5. Gere o Alvo
# Passo 1.5.1. Gere um círculo de fundo laranja
pygame.draw.circle(tela,'orange',(320,240),100,0)
# Passo 1.5.2. Imprima o círculo na tela
pygame.display.update()
# Passo 2. Marque na tela os lançamentos do dardo
atira = True
# Passo 2.1. Enquanto não terminar o jogo, lance o dardo
while atira:
# Passo 2.1.1. Leia a posição e eventos do mouse
   pygame.event.get()
   event = pygame.event.wait()
# Passo 2.1.2. Se o botão do mause foi pressionado
   if event.type == pygame.MOUSEBUTTONDOWN:
# Passo 2.1.2.1. Se o botão esquerdo foi pressionado
      if event.button == 1:
# Passo 2.1.2.1.1. Armazene as coordenadas do mouse
         x1, y1 = event.pos
# Passo 2.1.2.1.2. Verifique se as coordenadas estão no círculo
         if (x1-320)**2 + (y1-240)**2 <= 100**2:
# Passo 2.1.2.1.2.1. Marque as coordenadas (x1,y1) no círculo
            pygame.draw.circle(tela,'black',event.pos,1,0)
            pygame.display.update()
            playsound.playsound('laser.wav')
         else:
            pygame.draw.circle(tela,('black',event.pos,1,0)
            pygame.display.update()
# Passo 2.1.2.1.3. Se foi o botão direito
      elif event.button == 3:
         atira = False
# Passo 3. Imprima o jogo num arquivo e finalize o jogo
pygame.image.save(tela,'tiroaoalvo.png')
quit()

# pós: Um alvo com vários pontos marcados.
# fim do módulo principal