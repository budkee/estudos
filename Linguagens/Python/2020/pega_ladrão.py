print('Guarda Costeira: Será possivel alcançar o ladrão antes do limite das águas internacionais (12 milhas)?')

while True:
  try:
      D, Vf, Vg = list(map(int, input('Qual a distância, a velocidade do fugitivo e a da guarda costeira?: ').split()))
      n1 = D ** 2
      n2 = 12 ** 2
      dx = (n1 + n2) ** (1 / 2)
      tf = 12 / Vf
      tg = dx / Vg

      if tg <= tf:
          print('S')
      else:
          print('N')
  except EOFError:
    break

# D = int(input())
# dX = (12**2 + (D)**2)**1/2
# Vf = int(input('Qual é a velocidade do fugitivo?: '))
# tf = 12/Vf
# Vg = int(input('Qual é a velocidade da guarda costeira?: '))
# tg = dX/Vg
# if tg <= tf:
#    print('S')
# else:
#    print('N')
