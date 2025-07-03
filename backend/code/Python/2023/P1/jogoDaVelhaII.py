# Programa: jogodavelha01pygame.py
# Programador:
# Data: 30/03/2022
# Este programa utiliza a biblioteca Pygame. Ele gera e imprime um
# reticulado 3 x 3. O programa lê dois cliques do mouse e imprime
# dois movimentos, um para X e outro para O, e imprime as informações
# do jogo na tela.
# declaração das bibliotecas utilizadas
import pygame
import time
import playsound
# início do módulo principal
# descrição das variáveis utilizadas
# float x, y
# str text
# font fonte
# display tela

# pré: x, y posição do mouse na tela

# Passo 1. Defina o ambiente gráfico
# Passo 1.1. Defina as Cores
ORANGE = (255,150,0)
YELLOW = (255,200,0)
BLACK = (0, 0, 0)
RED = (255,0,0)
# Passo 1.2. Defina o tamanho da imagem/tela
largura = 800
altura = 500
# Passo 1.3. Inicialize o pygame
pygame.init()
# Passo 1.4. Crie a janela gráfica (tela)
tela = pygame.display.set_mode((largura, altura))
# Passo 1.5. Defina a cor do fundo da janela
tela.fill(ORANGE)
# Passo 1.6. Gere um tabuleiro para o jogo da velha
# Passo 1.6.1. Gere um retângulo de fundo laranja
pygame.draw.rect(tela, YELLOW, [100,100,300,300])
# Passo 1.6.2. Gere as linhas do grid
pygame.draw.line(tela, BLACK, [100,100],[400,100],3)
pygame.draw.line(tela, BLACK, [100,200],[400,200],3)
pygame.draw.line(tela, BLACK, [100,300],[400,300],3)
pygame.draw.line(tela, BLACK, [100,400],[400,400],3)
pygame.draw.line(tela, BLACK, [100,100],[100,400],3)
pygame.draw.line(tela, BLACK, [200,100],[200,400],3)
pygame.draw.line(tela, BLACK, [300,100],[300,400],3)
pygame.draw.line(tela, BLACK, [400,100],[400,400],3)
# Passo 1.7. Gere as mensagens
# Passo 1.7.1. Gere uma linha vertical separando o grid
pygame.draw.line(tela, BLACK, [500, 0], [500, 500],3)
# Passo 1.7.2. Defina o tipo e tamanho da letra para as mensagens
fonte = pygame.font.SysFont('arial', 20)
# Passo 1.7.3. Gere as mensagens
text = str('Bem vindo ao Jogo da Velha')
text = fonte.render(text, True, BLACK)
tela.blit(text, (550,100))
text = str('Clique numa célula para o')
text = fonte.render(text, True, BLACK)
tela.blit(text, (550,140))
text = str('próximo movimento, ou clique')
text = fonte.render(text, True, BLACK)
tela.blit(text, (550,180))
text = str('fora do reticulado para')
text = fonte.render(text, True, BLACK)
tela.blit(text, (550,220))
text = str('finalizar o jogo.')
text = fonte.render(text, True, BLACK)
tela.blit(text, (550,260))
pygame.display.flip()
# Passo 2. Leia os movimentos do Mouse
# Passo 2.1. Leia os dados da primeira jogada
# Passo 2.1.1. Iterrompa a execução por 5 segundos
time.sleep(5)
# Passo 2.1.2 Leia os eventos dos dispositivos de entrada
pygame.event.pump()
# Passo 2.1.3 Leia o botão do mouse
botoes = pygame.mouse.get_pressed()
# Passo 2.1.4. Armazene as coordenadas do mouse
x,y = pygame.mouse.get_pos()
# Passo 2.1.5. Se o botão esquerdo ou direito foi pressionado
if botoes[0] or botoes[2]:
# Passo 2.1.5.1. Verifique se as coordenadas estão no tabuleiro
   if x >= 100 and x <= 400 and y >= 100 and y <= 400:
# Passo 2.1.5.1.1. Marque o retângulo escolhido
      if x >= 100 and x < 200 and y >= 100 and y < 200:
         pygame.draw.rect(tela, RED, [100,100,100,100])
         pygame.display.update()
      elif x >= 200 and x < 300 and y >= 100 and y < 200:
         pygame.draw.rect(tela, RED, [200,100,100,100])
         pygame.display.update()
      elif x >= 300 and x <= 400 and y >= 100 and y < 200:
         pygame.draw.rect(tela, RED, [300,100,100,100])
         pygame.display.update()
      elif x >= 100 and x < 200 and y >= 200 and y < 300:
         pygame.draw.rect(tela, RED, [100,200,100,100])
         pygame.display.update()
      elif x >= 200 and x < 300 and y >= 200 and y < 300:
         pygame.draw.rect(tela, RED, [200,200,100,100])
         pygame.display.update()
      elif x >= 300 and x <= 400 and y >= 200 and y < 300:
         pygame.draw.rect(tela, RED, [300,200,100,100])
         pygame.display.update()
      elif x >= 100 and x < 200 and y >= 300 and y <= 400:
         pygame.draw.rect(tela, RED, [100,300,100,100])
         pygame.display.update()
      elif x >= 200 and x < 300 and y >= 300 and y <= 400:
         pygame.draw.rect(tela, RED, [200,300,100,100])
         pygame.display.update()
      elif x >= 300 and x <= 400 and y >= 300 and y <= 400:
         pygame.draw.rect(tela, RED, [300,300,100,100])
         pygame.display.update()
      playsound.playsound('laser.wav')
# Passo 2.1.5.2. Pressionou o mouse fora do tabuleiro
   else:
      print('finalize o jogo')
      quit()
# Passo 2.1.6. Não pressionou o mouse
else:
   print('não selecionou')
   quit()
# Passo 2.2. Leia os dados da segunda jogada
# Passo 2.2.1. Iterrompa a execução por 5 segundos
time.sleep(5)
# Passo 2.2.2 Leia os eventos dos dispositivos de entrada
pygame.event.pump()
# Passo 2.2.3 Leia o botão do mouse
botoes = pygame.mouse.get_pressed()
# Passo 2.2.4. Armazene as coordenadas do mouse
x,y = pygame.mouse.get_pos()
# Passo 2.2.5. Se o botão esquerdo ou direito foi pressionado
if botoes[0] or botoes[2]:
# Passo 2.2.5.1. Verifique se as coordenadas estão no tabuleiro
   if x >= 100 and x <= 400 and y >= 100 and y <= 400:
# Passo 2.2.5.1.1. Marque o retângulo escolhido
      if x >= 100 and x < 200 and y >= 100 and y < 200:
         pygame.draw.rect(tela, BLACK, [100,100,100,100])
         pygame.display.update()
      elif x >= 200 and x < 300 and y >= 100 and y < 200:
         pygame.draw.rect(tela, BLACK, [200,100,100,100])
         pygame.display.update()
      elif x >= 300 and x <= 400 and y >= 100 and y < 200:
         pygame.draw.rect(tela, BLACK, [300,100,100,100])
         pygame.display.update()
      elif x >= 100 and x < 200 and y >= 200 and y < 300:
         pygame.draw.rect(tela, BLACK, [100,200,100,100])
         pygame.display.update()
      elif x >= 200 and x < 300 and y >= 200 and y < 300:
         pygame.draw.rect(tela, BLACK, [200,200,100,100])
         pygame.display.update()
      elif x >= 300 and x <= 400 and y >= 200 and y < 300:
         pygame.draw.rect(tela, BLACK, [300,200,100,100])
         pygame.display.update()
      elif x >= 100 and x < 200 and y >= 300 and y <= 400:
         pygame.draw.rect(tela, BLACK, [100,300,100,100])
         pygame.display.update()
      elif x >= 200 and x < 300 and y >= 300 and y <= 400:
         pygame.draw.rect(tela, BLACK, [200,300,100,100])
         pygame.display.update()
      elif x >= 300 and x <= 400 and y >= 300 and y <= 400:
         pygame.draw.rect(tela, BLACK, [300,300,100,100])
         pygame.display.update()
      playsound.playsound('laser.wav')
# Passo 2.2.5.2. Pressionou o mouse fora do tabuleiro
   else:
      print('finalize o jogo')
      quit()
# Passo 2.2.6. Não pressionou o mouse
else:
   print('não selecionou')
   quit()
# Passo 3. Imprima o jogo num arquivo
pygame.image.save(tela,'jogodavelha01pygame.png')

# pós: Um tabuleiro com um jogo da velha, a seleção e a impressão de
#      dois movimentos.
# fim do módulo principal