lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))

# [1, 2, 3, 4, 5]
# [4, 5, 6, 7, 8]
# [1, 2, 3, 4, 5, 6, 7, 8]

for num in lista1:
    if num in lista2:
        lista2.remove(num)

lista1.extend(lista2)
print(lista1)