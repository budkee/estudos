tam1 = int(input())
ap1 = list(map(int, input().split()))
tam2 = int(input())
isd = list(map(int, input().split()))

interseccao = []
for rga in ap1:
    if rga in isd:
        interseccao.append(rga)

print(interseccao)