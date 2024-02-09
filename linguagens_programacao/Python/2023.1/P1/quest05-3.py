num1 = 10
num2 = 5
if (num1 < num2) or (num2 - num1) < 0:
   temp = num1
   num1 = num2
   num2 = temp
total = num1*num2 + num2
print(total)