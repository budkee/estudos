# -*- coding: utf8 -*-
# Programa: retas01pyg.py
# Programador:
# Data: 27/09/2020
# Este programa gera um conjunto de retas numa janela gráfica. Mudando
# a inclinação das retas o programa cria um efeito nas retas geradas.
# O programa usa o módulo pygame
# início do módulo principal
# declaração das bibliotecas utilizadas
import pygame

# descrição das variáveis utilizadas
# int n
# display tela

# pré: n

# Passo 1. Leia o número de retas, inicialize o pygame e defina a janela
# Passo 1.1. Leia o número de retas
n = int(input())
# Passo 1.2. Inicialize o pygame
pygame.init()
# Passo 1.3. Defina a janela
tela = pygame.display.set_mode((640, 640))
# Passo 1.4. Defina a cor branca do fundo do painel
tela.fill('white')
# Passo 2. Gere as n retas
# Passo 2.1. Para i em [0,640] passo 20 repita
for i in range(0, n + 1, 20):
    # Passo 2.1.1. Gere uma linha (i,640) a (0,i)
    pygame.draw.line(tela, 'black', (i, 640), (0, i), 1)
    # Passo 2.2. Imprima a linha na tela
    pygame.display.update()

# pós: um conjunto de retas na tela
# fim do módulo principal