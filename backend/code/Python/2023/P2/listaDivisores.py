# Função para determinar os divisores de um número
def divisores(num):
    lista = []
    qualquer = 1  # num % 1 == 0
    for i in range(1, num): # range(start, stop, step
        # Passo 2.3: construa a condicional para o termômetro
        if num % i == 0:
            #print(num, i)
            lista.append(i)  # Adicione na lista dos divisores
        else:
            pass
    return lista

num = int(input())
print(divisores(num))
