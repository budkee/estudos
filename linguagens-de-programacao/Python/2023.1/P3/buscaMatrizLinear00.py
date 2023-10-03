# Método de busca: linear
# A busca linear percorre todos os elementos de uma lista, sequencialmente,
# para encontrar um valor de interesse.

# Problema: reservar assentos em suas aeronaves
# Programa: Mapa de assentos de um avião

# Objetivo: O programa deve ler as informações relativas ao número de fileiras [1, 12] e
# cadeiras [A, D] em cada fileira. Em seguida, ele deve verificar se estão ou não
# ocupadas. Caso não estejam, ele solicita o código do assento de interesse do usuário
# para fazer a reserva. O programa termina ao receber como resposta um valor diferente
# de "S" ou "s", imprimindo o mapa de assentos atualizado.

# Procedimento a ser executado pelo programa:

# 1. O programa deverá fazer a leitura de todos os assentos do avião, verificando os
# que estão ocupados(1) e os que estão desocupados(0).
#   1.1 Entre com as dimensões do avião (12, 4):
l, c = map(int, input().split())
#   1.2 Inicialize as estruturas de dados, neste caso a matriz referente aos assentos:
assentos = [[0]*c for i in range(l)]
#   1.3 Leia a atual situação dos assentos, linha a linha:
for i in range(0,l):
    assentos[i] = list(map(int, input().split()))

# 2. Leia as reservas de assentos
# 2.1. Leia se o usuário quer fazer uma reserva
resposta = input()
# 2.2 Enquanto a resposta for "S" ou "s":
while resposta.upper() == 'S':
#   2.2.1 Leia a reserva:
    reserva = input()
#   2.2.2. Compute o tamanho da entrada
    tam = len(reserva)
#   2.2.3. Obtenha o número da fileira desejada
    fila = int(reserva[0:tam-1])-1
#   2.2.4. Obtenha o lugar desejado (último char da entrada)
    poltronas = ['A', 'B', 'C', 'D']
    pos = poltronas.index(reserva[tam-1])
#   2.2.5. Verifique se o assento desejada não existe
    if fila >= l or pos >= c or pos is not poltronas:
        print(reserva,'assento inexistente')
#   2.2.6. Verifique se o assento desejado está disponível
    elif assentos[fila][pos] == 0:
        assentos[fila][pos] = 1 # reserve o assento
        print(reserva,'reserva efetuada')
#   2.2.7. Verifique se o assento desejado está ocupado
    else:
        print(reserva,'assento ocupado')
#   2.2.8. Leia se o usuário quer fazer uma reserva
    resposta = input()
# 3. Imprima o mapa de ocupação da aeronave
print('  ',poltronas)
for i in range(l):
    print('{0:2d}'.format(i+1),list(map(str,assentos[i])))

