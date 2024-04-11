horas = float(input("Quantas horas de trabalho do funcionário?"))
salario = float(input("Qual é o salário do funcionário por hora?"))

resultado = salario * horas

print("O valor a ser pago para o funcionario é de R${}".format(resultado))
print("Após 40h trabalhadas, o salário aumenta em 50% por hora extrapolada")
print("Portanto:")

hadd = float(input("Quantas horas adicionais?"))

reajuste = float((salario * 40) + (hadd * salario * 50/100))

print("Após 40h de trabalho, o valor do salario com adicional de 50% por hora será {}".format(reajuste))
