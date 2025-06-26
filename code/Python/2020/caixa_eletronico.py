
print('>> Caixa eletrônico << \n'
      '\nNotas disponíveis para saque:'
      '\nR$200'
      '\nR$100'
      '\nR$50'
      '\nR$20\n')

valor = int(input('Quantos R$ voce quer sacar?: '))

total = valor
nota_max = 200
nota_min = 20
notas_dadas = 0  # Ainda nao te dei nenhuma nota;

while True:
    if valor >= nota_min:

        try:
            if total >= nota_max:  # Ou seja, se o valor atribuido for maior ou igual a nota(R$) maxima que eu posso te dar
                total -= nota_max  # O novo total sera o valor atribuido menos a nota maxima (200);
                notas_dadas += 1  # A contagem das notas dadas será atribuida a variavel notas_dadas a cada vez que eu retirar 200 reais do valor atribuido;

            else:  # Se não der para retirar "200" do valor; #Qual será a nota que me restou?

                print('{} notas de R${}'.format(notas_dadas, nota_max))

                if nota_max == 200:
                    nota_max = 100
                elif nota_max == 100:
                    nota_max = 50
                elif nota_max == 50:
                    nota_max = 20

                notas_dadas = 0  # Toda vez que ele fechar o ciclo de uma nota max, zera as notas dadas
                if total == 0:
                    break

        except ValueError:
            print('Não disponível nesse valor')
            break

    else:
        print('Não disponível nesse valor')
        break
