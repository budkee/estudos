def dist(x1, x2, y1, y2):
    deltax = (x2 - x1) ** 2
    deltay = (y2 - y1) ** 2
    d = (deltax + deltay) ** 1 / 2
    return d

x1, y1 = input('Insira as coordenadas bidimensionais de um ponto(x1,y1): ').split(' ')
x2, y2 = input('Insira as coordenadas bidimensionais de um outro ponto(x2,y2): ').split(' ')

x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

print('A distancia entre P({},{}) e Q({},{}) é = {}'.format(x1, y1, x2, y2, dist(x1, x2, y1, y2)))

