# Digite o tamanho da sequência
tam = int(input())

# Leia os números
lista = list(map(int, input().split()))

# Inicialize a mensagem
msg = ''

# Verifique se é cheio ou não
for i in range(tam-1):
    
    dif = abs(lista[i+1] - lista[i])
    if dif < 1 or dif >= tam:
        msg = 'N'
    else:
        msg = 'C'

print(msg)

