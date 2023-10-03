def dist(v,t):
    d = v * t
    return d

v = int(input('Qual a Velocidade(Km/h) do objeto? '))
t = int(input('Qual foi o Tempo(h) percorrido?' ))

print('A distância percorrida foi: {} Km'.format(dist(v,t)))
