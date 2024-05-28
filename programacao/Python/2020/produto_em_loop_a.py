a = 1
for i in [1, 2, 3, 4, 5]:
    i = float(i)
    a *= i    # [a *= i] é o mesmo que [a = a * i]
print('fatorial de 5 = {:2}'.format(a))
