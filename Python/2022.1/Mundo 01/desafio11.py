larg = int(input('Digite a largura da parede: ')) 
alt = int(input('Digite a altura da parede: '))
area = larg * alt
tinta_necessaria = area / 2

print('A quantidade necessária para pintar essa parede é/são {} litros de tinta '.format(tinta_necessaria))