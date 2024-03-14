# Programa: jogodavelha00pygame.py
# Programador:
# Data: 30/03/2022
# Este programa utiliza a biblioteca Pygame. Ele gera e imprime um
# reticulado 3 x 3. O programa também imprime dois movimentos,
# um para X e outro para O, e imprime as informações do jogo na tela.
# declaração das bibliotecas utilizadas
import pygame
# início do módulo principal
# descrição das variáveis utilizadas
# float x1, y1, x2, y2
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
# Passo 1.3. Atribua as coordenadas dos movimentos
x1, y1 = 135, 130
x2, y2 = 235, 130
# Passo 1.4. Inicialize o pygame
pygame.init()
# Passo 1.5. Crie a janela gráfica (tela)
tela = pygame.display.set_mode((largura, altura))
# Passo 1.6. Defina a cor do fundo da janela
tela.fill(ORANGE)
# Passo 1.7. Gere um tabuleiro para o jogo da velha
# Passo 1.7.1. Gere um retângulo de fundo laranja
pygame.draw.rect(tela, YELLOW, [100,100,300,300])
# Passo 1.7.2. Gere as linhas do grid
pygame.draw.line(tela, BLACK, [100,100],[400,100],3)
pygame.draw.line(tela, BLACK, [100,200],[400,200],3)
pygame.draw.line(tela, BLACK, [100,300],[400,300],3)
pygame.draw.line(tela, BLACK, [100,400],[400,400],3)
pygame.draw.line(tela, BLACK, [100,100],[100,400],3)
pygame.draw.line(tela, BLACK, [200,100],[200,400],3)
pygame.draw.line(tela, BLACK, [300,100],[300,400],3)
pygame.draw.line(tela, BLACK, [400,100],[400,400],3)
# Passo 1.7.3. Gere uma linha vertical separando o grid
pygame.draw.line(tela, BLACK, [500, 0], [500, 500],3)
# Passo 1.7.4. Gere as Instruções
# Passo 1.7.4.1. Defina o tipo e tamanho da letra para as mensagens
fonte = pygame.font.SysFont('arial', 20)
# Passo 1.7.4.2. Gere as mensagens
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
# Passo 2. Gere e imprima os movimentos no tabuleito
# Passo 2.1. Gere a primeira jogada
fonte = pygame.font.SysFont('arial', 40)
text = str('O')
text = fonte.render(text, True, RED)
tela.blit(text, (x1,y1))
pygame.display.update()
# Passo 2.2. Gere a segunda jogada
text = str('X')
text = fonte.render(text, True, BLACK)
tela.blit(text, (x2,y2))
pygame.display.update()
# Passo 3. Imprima o jogo na tela
tela.show()
# pós: Um tabuleiro com um jogo da velha e a impressão de
# dois movimentos.
# fim do módulo principal