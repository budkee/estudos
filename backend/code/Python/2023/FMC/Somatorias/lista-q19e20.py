# Seja a sequência {a_n} == {a_n = 3 ** n}. Implemente um código python de uma somatória com o intervalo i de [0,100] para o termo a_i.
# Início do código
# 1. Inicialize as variáveis
s = 0
# 2. Construa a somatória
for i in range(0, 101):
    eq = 3**i
    s += eq
# 3. Imprima o resultado
print('O valor da somatória é: {}'.format(s))