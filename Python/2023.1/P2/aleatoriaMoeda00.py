# Simulação da jogada de uma moeda: para cada jo

import random
# Entre com o a semente da jogada:
semente = random.seed(int(input()))
# Número de jogadas = 100

# Inicialize a moeda e o resultado
cara = 'Ca'
coroa = 'Co'
moeda = [cara, coroa]
jogadas = ''

somaPremios = 0
premiosObtidos = 0
jogada = 1

while jogada <= 100:
    print('nº da jogada = {}'.format(jogada))
# Gere o numero n da jogada na qual a primeira cara aparece:
    resultJogada = random.choice(moeda)
    # Se a moeda for cara, calcule o premio final:
    if resultJogada == cara:
        premio = 2 * jogada
        somaPremios += premio
        premiosObtidos += 1
        jogadas += resultJogada
    # Se for coroa, agregue a jogada ao resultado final
    else:
        jogadas += resultJogada
    # Feche o loop
    print('Moeda = {}'.format(resultJogada))
    print('premios = {}'.format(somaPremios))
    print('Jogadas = {}\n'.format(jogadas))
    jogada += 1
    

media = somaPremios/premiosObtidos
print(media)
