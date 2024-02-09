# -*- coding: utf-8 -*-
# Programa: bouncingball.py
# Programa do Livro Sedgewick e Wayne
# Este programa utiliza o módulo stddraw (pygame).
# Ele simula o movimento de uma bola ricocheteando num 
# retângulo com coordenadas entre -1 e +1. A bola ricocheteia nas bordas 
# do retângulo de acordo com as leis de elasticidade de colisão. Os 20
# milissegundos de espera (stddraw.show(20)) mantém a imagem da
# bola persistente na tela, mesmo se os pixeis da bola alternam entre
# branco e preto.
# Declaração dos módulos utilizados
import stddraw

# inicialização das constantes e variáveis
RADIUS = .05
DT = 20.0

rx = .480
ry = .860
vx = .015
vy = .023

# Passo 1. Defina a escala do sistema de coordenadas   
stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)
# Passo 2. Laço de geração da animação
while True:
# Passo 2.1. Atualize a posição da bola com as leis de elasticidade de colisão
    if abs(rx + vx) + RADIUS > 1.0:
        vx = -vx
    if abs(ry + vy) + RADIUS > 1.0:
        vy = -vy
    rx = rx + vx
    ry = ry + vy
# Passo 2.2. Apague o fundo
    stddraw.clear(stddraw.GRAY)
# Passo 2.3. Desenhe a bola na tela
    stddraw.filledCircle(rx, ry, RADIUS)
# Passo 2.4. Imprima a bola e faça uma pausa por 20 milesegundos
#    stddraw.show(0)
    stddraw.show(20)
    
# fim


