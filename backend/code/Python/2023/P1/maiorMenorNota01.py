nota = float(input("Digite a primeira nota: "))
maior_nota = menor_nota = nota
soma_notas = nota
quantidade_notas = 1

nota = float(input("Digite a próxima nota (digite um número negativo para encerrar): "))

while nota >= 0:
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota
    soma_notas += nota
    quantidade_notas += 1
    nota = float(input("Digite a próxima nota (digite um número negativo para encerrar): "))

media_notas = soma_notas / quantidade_notas

print("Maior nota: %.2f" % maior_nota)
print("Menor nota: %.2f" % menor_nota)
print("Média das notas: %.2f" % media_notas)