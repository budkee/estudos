# Seja a sequência {a_n} == {a_n = 3 ** n - 2 ** n}. Implemente um código python de uma somatória com o intervalo i de [0,100] para o termo a_i.

# Início do código A [REVISAR]
# 1. Inicialize as variáveis
s = 0
t1 = 0
t2 = 0
# 2. Construa a somatória
for i in range(2, 10):
    t1 += i
    t2 += 2 ** i
s = t1 * 3 - t2
# 3. Imprima o resultado
print('O valor da somatória é: {}'.format(s))
# Saída esperada:
# pela fórmula fechada do caderno: -890
# pelo loop acima: -888
