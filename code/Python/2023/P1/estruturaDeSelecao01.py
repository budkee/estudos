# Passo 1: leitura da entrada
rga = input('Digite seu RGA: ')
freq = int(input('Insira a frequência do estudante: '))
n1, n2, n3 = map(float, input('Digite as notas [P1, P2 e P3]: ').split())
t1, t2 = map(float, input('Digite a nota do primeiro trabalho [T1]: ').split())
# Passo 2: compute os valores e desenhe a estrutura
# Passo 2.1: computando os valores
nf = (n1 + n2 + n3)/3
tf = (t1 + t2)/2
mf = round((0.75*nf) + (0.25*tf), 1)
# Passo 2.2: desenhe a estrutura
if freq >= 75:
    if mf >= 6:
        msg = 'AP'
    else:
        msg = 'RN'
else:
    msg = 'RF'
# print("I'm sorry my dear but you're up for elimination. (Cortesia de Ru Paul's Drag Race)")
# Passo 3: leitura da saida
print('RGA: {}\n'
      'Média: {}\n'
      'Resultado: {}'.format(rga, mf, msg))

