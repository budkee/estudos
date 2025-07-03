# Campo Minado
# Programa: campominado.py
# Programador:
# Data: 16/11/2019
# Este programa lê as dimensão e gera um mini campo minado. O
# programa lê as tentativas do usuário e encerra o programa se a
# tentativa encontrou uma bomba ou se o usuário conseguiu achar 3
# posições em bombas. O programa imprime uma mensagem
# informando o resultado e a configuração final do jogo.
# início do módulo principal
# módulos utilizados
import random

# descrição das variáveis utilizadas
# list campo[[]] - lista de listas para representar campo
# int m, n - dimensões do campo minado
# int x, y - coordenadas selecionadas
# int acertos - número de acerto do jogador
# bool bomba - indica que tem uma bomba
# str msg - mensagem ao jogador

# pré: lin col

# Passo 1. Crie o campo minado
# Passo 1.1. Leia as dimensões do campo
lin, col = map(int, input().split())
# Passo 1.2. Gere o campo minado
random.seed()
valores = [0, 1]
campo = [random.choices(valores, weights=[7, 3], k=col) for i in range(lin)]
# Passo 2. Inicie o jogo
# Passo 2.1. Inicialize as variáveis
bomba = False  # antes do início não encontrou bomba
acertos = 0
# Passo 2.2. Enquanto bomba = 0 e acertos < 3 faça
while not bomba and acertos < 3:
    # Passo 2.2.1. Leia as coordenadas da tentativa
    x, y = map(int, input().split())
    # Passo 2.2.2. Verifique se a posição tem bomba
    if campo[x - 1][y - 1] == 1:
        bomba = True
        print('BOMBA!!!')
    # Passo 2.2.3. Se a posição não é bomba
    elif campo[x - 1][y - 1] == 0:
        print('ACERTOU!!')
        acertos = acertos + 1
        campo[x - 1][y - 1] = 2
    # Passo 2.2.4. Posição já testada
    else:
        print('POSIÇÃO JÁ TESTADA!!!')
    # Passo 2.2.5. Verifique se o jogador ganhou o jogo
if acertos == 3:
    msg = 'GANHOU!!!'
else:
    msg = 'PERDEU!!!'

# Passo 3. Imprima o resultado
# Passo 3.1. Imprima a mensagem
print(msg)
# Passo 3.2. Imprima o campo minado resultante
print('  ', end='')  # imprime dois espaços e não muda de linha
for i in range(col):  # cabeçalho superior
    print('{:3d}'.format(i + 1), end='')
print()  # começa uma nova linha
for i in range(lin):  # número da linha e campo[i]
    print('{0:2d}'.format(i + 1), campo[i])

# pós: 'GANHOU!!!' ande acertos == 3 || 'PERDEU!!!'
#      para i em {0..lin-1}: para j em {0..col-1}:campo[i][j]
# fim do módulo principal
