# Sobre: Este programa lê as notas das avaliações da disciplina de PROG1 e retorna a média final do aluno.
# Programador: bSirius

# Formato de entrada
# 7.5
# 8.2
# 6.4
# 9.0
# 8.0

# Formato de saida
# Primeira prova    7.5
# Segunda prova     8.2
# Terceira prova    6.5
# Média provas      7.4
# Primeiro trabalho 9.0
# Segundo trabalho  8.0
# Média trabalhos   8.5
# ---------------------
# Média Final       7.7

# Constantes e variaveis
# float: p1, p2, p3, mp, t1, t2, mt, mf

# Passo 1: leia os valores das três provas e dos dois trabalhos
p1 = float(input('Nota da primeira prova: '))
p2 = float(input('Nota da segunda prova: '))
p3 = float(input('Nota da terceira prova: '))
t1 = float(input('Nota do primeiro trabalho: '))
t2 = float(input('Nota do segundo trabalho: '))
# Passo 2: calcule a media das provas, dos trabalhos e a média final
mp = (p1 + p2 + p3)/3
mt = (t1 + t2)/2
mf = 0.75 * mp + 0.25 * mt
# Passo 3: imprima os valores finais
print('\nPrimeira prova:      {:.1f}\n'
      'Segunda prova:       {:.1f}\n'
      'Terceira prova:      {:.1f}\n'
      '---------------------------\n'
      'Média provas:        {:.1f}\n' \
      '\n' \
      'Primeiro trabalho:   {:.1f}\n' \
      'Segundo trabalho:    {:.1f}\n' \
      '-----------------------\n'
      'Média trabalhos:     {:.1f}\n'
      '\n'
      'Média final:         {:.1f}'.format(p1,p2,p3,mp,t1,t2,mt,mf))