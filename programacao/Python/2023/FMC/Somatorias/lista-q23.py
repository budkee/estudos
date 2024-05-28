# Seja a sequência {a_n} == {a_n = 3 ** n - 2 ** n}. Implemente um código python de uma somatória com o intervalo i de [0,100] para o termo a_i.

# Início do código [REVISAR]
# 1. Inicialize as variáveis
n = int(input('Digite o início da soma: '))
m = int(input('Digite o final da soma: '))

# 2. Construa a somatória pela fórmula fechada dos respectivos termos da equação
# 2.1 Declare as fórmulas do primeiro termo (t1) e o conjunto do segundo termo (t2a e t2b)
t1 = 3 * ((m*(m+1) / 2) - (n*(n+1) / 2))
t2a = (1 * (2 ** (m+1)) - 1) / 2 - 1
t2b = (1 * (2 ** (n+1)) - 1) / 2 - 1
# 2.2 Compute a somatória {s = t1 - t2}
s = t1 - (t2a - t2b)
# 3. Imprima o resultado
print('O valor da somatória é: {}'.format(s))
# Saída esperada:
# pela fórmula fechada do caderno: -890
# pelo loop em (lista-q22.py): -888
# pela fórmula fechada em (lista-q22-formula_fechada.py): -382