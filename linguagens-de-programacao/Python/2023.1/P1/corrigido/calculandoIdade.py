# Este programa lé a data de nascimento de uma pessoa e calcula quantos anos ela tem.

# Entrada: data de referência: dd/mm/aaaa e data de nascimento: dd/mm/aaaa
# Saída: Essa pessoa tem xx anos de idade.

# Variáveis: int; dian, mesn, anon, diar, mesr, anor, idade

# Declaração das Funções
def idade(diar, mesr, anor, dian, mesn, anon):
    # Passo 2.1: Calcule a diferença entre os anos
    idade = anor - anon
    # Passo 2.2: Verifique se o mês e o dia já passou
    if mesn > mesr:
        idade -= 1
    elif mesn == mesr and (dian < diar):
        idade -= 1

    return idade
# Início do módulo principal

# Passo 1: leia a entrada
diar, mesr, anor = map(int, input('Data de referência: ').split('/'))
dian, mesn, anon = map(int, input('Data de nascimento: ').split('/'))

# Passo 2: calcule a idade
idade = idade(diar, mesr, anor, dian, mesn, anon)

# Passo 3: Imprima a saída
print('A pessoa tem {} anos de idade.'.format(idade))

# Fim do módulo principal