# -*- coding: utf-8 -*-

# Passo 1: leitura dos ângulos
g1, m1, s1 = map(int, input().split())
g2, m2, s2 = map(int, input().split())
# Passo 2: Compute os valores
# Passo 2.1: Soma dos segundos
segundos = (s1 + s2) % 60  # Computa para o resultado final
# Passo 2.2: Cálculo dos minutos restantes e dos minutos a serem adicionados
minutos = (s1 + s2) // 60  # Retorna a divisão inteira para ser adicionado no total dos minutos
minutos_total = (m1 + m2 + minutos) % 60  # Computa para o resultado final
# Passo 2.3: Cálculo do grau restante e do grau a ser adicionado
graus = (m1 + m2 + minutos) // 60    # Retorna a divisão inteira para ser adicionado no total do grau
grau_total = (g1 + g2 + graus) % 360  # Acrescimo do que sobrou dos minutos

# Passo 3. Imprima a soma
print('{0:3d} Graus {1:2d} Minutos {2:2d} Segundos +'.format(g1, m1, s1))
print('{0:3d} Graus {1:2d} Minutos {2:2d} Segundos ='.format(g2, m2, s2))
print('{0:3d} Graus {1:2d} Minutos {2:2d} Segundos'.format(grau_total,minutos_total,segundos))
