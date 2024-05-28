def fprimo(n):
    # Método mais trivial e menos eficaz para descobrir o número primo
    div = 2
    while n % div != 0:
        div += 1
    if n == div:
        msg = 'primo'
    else:
        msg = 'não primo'
    return msg

num = int(input())
msg =fprimo(num)
print(msg)