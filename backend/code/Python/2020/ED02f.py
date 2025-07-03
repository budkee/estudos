print('Atribuição de uma nota alfabética')
score = float(input('Insira a nota: '))

if score == 10.0:
    print('A')
elif score > 10:
    print('Nota incorreta, por favor, selecione uma nota entre 0 e 10.')
elif score >= 9.0:
    print('A')
elif score >= 8.0:
    print('B')
elif score >= 7.0:
    print('C')
elif score >= 6.0:
    print('D')
elif score < 0:
    print('Nota incorreta, por favor, selecione uma nota entre 0 e 10.')
elif score < 6.0:
    print('F')

print('Fim do programa')
