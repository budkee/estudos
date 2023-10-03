# Passo 1: Leia o valor do emprestimo a taxa anual e o pagamento efetuado
emprestimo = float(input())
jurosAnual = float(input())
pagMensal = float(input())
# Passo 2: Compute o juro mensal e o saldo devedor
# Passo 2.1: Compute o primeiro juros mensal
saldo = emprestimo
numPag = 0
totalJuros = 0
# Passo 2.3: Construa o loop para os outros pagamentos
print("Pagamento No.  Pagamento    Juros Saldo Devedor")
print('================================================')
while saldo > 0: # Enquanto o saldo for maior que 0, faça:

    # Calcule o juros referente ao saldo:
    jurosMensal = jurosAnual/1200 * saldo # É a porcentagem, dado pela taxa anual de juros dividido por 12 meses, referente ao saldo devedor
    totalJuros += jurosMensal
    saldo = saldo + jurosMensal - pagMensal
    numPag += 1
    # Debite o pagamento mensal:
    if saldo < 0:
        pagMensal = pagMensal + saldo
        saldo = 0

    # Passo 3: Imprima o numero do pagamento, o pagamento efetuado, o juros mensal e o saldo devedor
    print("{0:5d}{1:19.2f}{2:10.2f}{3:14.2f}".format(numPag, pagMensal, jurosMensal, saldo))

print("\n\nTotal de Juros = {0:12.2f}".format(totalJuros))