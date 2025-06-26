# Entrada e declaração das variáveis
import math
num = int(input('')) 

# Fatoração prima

# Um número é primo se ele só for divisível por 1 e por ele mesmo.
if num%1 and num//12 == 0: # Se o número for primo, faça:
    print(f"{num:d} = {num:d} primo")
    exit()
else: # Se o número não for primo, realiza a fatoração prima
    fatorial = 1
    for i in range(1, num+1):
        fatorial *= i
        print('Num{0:d} = {}'.format(num, fatorial))
    
