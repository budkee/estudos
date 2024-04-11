# Programa: jogodavelha02pygame.py
# Programador:
# Data: 30/03/2022
# Este programa utiliza a biblioteca Pygame. Ele gera e imprime um
# reticulado 3 x 3. O programa lê um conjunto de cliques do mouse e
# imprime os movimentos, um para X e outro para O, e imprime as
# informações jogo na tela.
# declaração das bibliotecas utilizadas
import pygame  # >= v.2.0
import playsound

# início do módulo principal
# descrição das variáveis utilizadas
# int rodada
# bool jogada
# str cor, text
# mouse botoes, x, y
# font fonte
# display tela

# pré: x, y posição do mouse na tela em cada jogada

# Passo 1. Defina o ambiente gráfico
# Passo 1.1. Defina o tamanho da imagem/tela
largura = 800
altura = 500
# Passo 1.2. Inicialize o pygame
pygame.init()
# Passo 1.3. Crie a janela gráfica (tela)
tela = pygame.display.set_mode((largura, altura))
# Passo 1.4. Defina a cor do fundo da janela
tela.fill('orange')
# Passo 1.5. Gere um tabuleiro para o jogo da velha
# Passo 1.5.1. Gere um retângulo de fundo laranja
pygame.draw.rect(tela, 'yellow', [100, 100, 300, 300])
# Passo 1.5.2. Gere as linhas do grid
pygame.draw.line(tela, 'white', [100, 100], [400, 100], 3)
pygame.draw.line(tela, 'white', [100, 200], [400, 200], 3)
pygame.draw.line(tela, 'white', [100, 300], [400, 300], 3)
pygame.draw.line(tela, 'white', [100, 400], [400, 400], 3)
pygame.draw.line(tela, 'white', [100, 100], [100, 400], 3)
pygame.draw.line(tela, 'white', [200, 100], [200, 400], 3)
pygame.draw.line(tela, 'white', [300, 100], [300, 400], 3)
pygame.draw.line(tela, 'white', [400, 100], [400, 400], 3)
# Passo 1.6. Gere as mensagens
# Passo 1.6.1. Gere uma linha vertical separando o grid
pygame.draw.line(tela, 'black', [500, 0], [500, 500], 3)
# Passo 1.6.2. Desenhe as linas na tela
pygame.display.flip()
# Passo 1.6.3. Defina o tipo e tamanho da letra para as mensagens
fonte = pygame.font.SysFont('arial', 20)
# Passo 1.6.4. Gere as mensagens e escreva na tela
text = str('Bem vindo ao Jogo da Velha')
text = fonte.render(text, True, 'black')
tela.blit(text, (550, 100))
text = str('Clique numa célula para o')
text = fonte.render(text, True, 'black')
tela.blit(text, (550, 140))
text = str('próximo movimento, ou clique')
text = fonte.render(text, True, 'black')
tela.blit(text, (550, 180))
text = str('fora do reticulado para')
text = fonte.render(text, True, 'black')
tela.blit(text, (550, 220))
text = str('finalizar o jogo.')
text = fonte.render(text, True, 'black')
tela.blit(text, (550, 260))
# Passo 2. Marque no tabuleiro as escolhas dos movimentos
# Passo 2.1. Inicialize o primeiro movimento
jogada = True
rodada = 1
cor = 'red'
# Passo 2.2. Enquanto não terminar o jogo, faça
while jogada:
    # Passo 2.2.1. Leia os eventos do mouse
    pygame.event.pump()
    # Passo 2.2.2 Leia o botão do mouse
    botoes = pygame.mouse.get_pressed()
    # Passo 2.2.3. Armazene as coordenadas do mouse
    x, y = pygame.mouse.get_pos()
    # Passo 2.2.4. Se o botão esquerdo ou direito foi pressionado
    if botoes[0] or botoes[2]:
        # Passo 2.2.4.1. Verifique se as coordenadas estão no tabuleiro
        if x >= 100 and x <= 400 and y >= 100 and y <= 400:
            # Passo 2.2.4.1.1. Marque o retângulo escolhido
            if x >= 100 and x < 200 and y >= 100 and y < 200:
                pygame.draw.rect(tela, cor, [102, 102, 98, 98])
                rodada = rodada + 1
                pygame.display.update()
            elif x >= 200 and x < 300 and y >= 100 and y < 200:
                pygame.draw.rect(tela, cor, [202, 102, 98, 98])
                rodada = rodada + 1
                pygame.display.update()
            elif x >= 300 and x <= 400 and y >= 100 and y < 200:
                pygame.draw.rect(tela, cor, [302, 102, 98, 98])
                rodada = rodada + 1
                pygame.display.update()
            elif x >= 100 and x < 200 and y >= 200 and y < 300:
                pygame.draw.rect(tela, cor, [102, 202, 98, 98])
                rodada = rodada + 1
                pygame.display.update()
            elif x >= 200 and x < 300 and y >= 200 and y < 300:
                pygame.draw.rect(tela, cor, [202, 202, 98, 98])
                rodada = rodada + 1
                pygame.display.update()
            elif x >= 300 and x < 400 and y >= 200 and y < 300:
                pygame.draw.rect(tela, cor, [302, 202, 98, 98])
                rodada = rodada + 1
                pygame.display.update()
            elif x >= 100 and x < 200 and y >= 300 and y <= 400:
                pygame.draw.rect(tela, cor, [102, 302, 98, 98])
                rodada = rodada + 1
                pygame.display.update()
            elif x >= 200 and x < 300 and y >= 300 and y <= 400:
                pygame.draw.rect(tela, cor, [202, 302, 98, 98])
                rodada = rodada + 1
                pygame.display.update()
            elif x >= 300 and x <= 400 and y >= 300 and y <= 400:
                pygame.draw.rect(tela, cor, [302, 302, 98, 98])
                rodada = rodada + 1
                pygame.display.update()
            playsound.playsound('laser.wav')
        # Passo 2.2.4.2. Pressionou o mouse fora do tabuleiro
        else:
            print('finalize o jogo')
            jogada = False
        # Passo 2.2.4.3. Defina a cor da próxima jogada
        if rodada % 2 == 0:
            cor = 'black'
        else:
            cor = 'red'
# Passo 3. Imprima o jogo num arquivo e finalize o jogo
pygame.image.save(tela, 'jogodavelha02pygame.png')
quit()

# pós: Um tabuleiro com um jogo da velha, a seleção e a impressão de
#      um conjunto de movimentos.
# fim do módulo principal
