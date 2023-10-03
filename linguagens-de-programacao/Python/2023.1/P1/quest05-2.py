num1 = 55
num2 = 33
soma = 0
if num1 < num2:
   num1 = num1 + num2
   soma = soma + num1 + num2
else:
   num2 = num1 + num2
   soma = soma + num1 + num2
print(soma)