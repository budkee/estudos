tam1 = int(input())
a = list(map(int, input().split()))
tam2 = int(input())
b = list(map(int, input().split()))

inter = []

for elemento in a:
    if elem in b:
        inter.append(elemento)

print(inter)