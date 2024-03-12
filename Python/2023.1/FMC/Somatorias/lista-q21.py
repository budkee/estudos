# Seja a sequência {a_n} == {a_n = 3 * n - 8}. Implemente um código python de uma somatória com o intervalo i de [n,m] para o termo a_i, de modo que m e n sejam entradas do usuário.

# Início do código
# 1. Inicialize as variáveis
n = int(input('Digite o início da soma: '))
m = int(input('Digite o final da soma: '))

# 2. Construa a somatória
# 2.1 Declare as fórmulas do primeiro termo (t1) e do segundo termo (t2)
t1 = 3 * ((m*(m+1)/2) - (n*(n+1)/2))
t2 = 8 * (m-n)
# 2.2 Compute a somatória {s = t1 - t2}
s = t1 - t2

# 3. Imprima o resultado
print('O valor da somatória é: {}'.format(s))