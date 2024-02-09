def piso_log2(num):
    pot2 = 1
    res1 = 0
    while pot2 <= num:
        res1 += 1
        pot2 = pot2*2
    res1 -= 1
    return res1


num = int(input())
piso = piso_log2(num)
print(piso)