x, y = list(input().split())
while x != y:
    x = int(x)
    y = int(y)
    try:
        if x > y:
            print('Decrescente')
            break
        else:
            print('Crescente')
            break
    except EOFError:
            break

print('Obrigada!')