# Sobre: Este programa lê o valor do crédito pré-existente na linha telefônica e a duração de uma chamada efetuada para outra operadora. Em seguida, calcula o valor da chamada, o valor dos impostos, o valor total da chamada e o saldo dos créditos da linha após a ligação.
# Programador: bSirius

# Formato de entrada:
# 22.78
# 3.45

# Formato de saída:
# Valor dos Créditos: R$ 22.78
# Valor da Chamada: R$ 6.20
# Valor dos Impostos: R$ 1.15
# Valor total da chamada: R$ 7.35
# Valor do Saldo Atual: R$ 15.43

# Constantes e variáveis
# float: alíquota do imposto (imposto), custo do minuto (custoMin), saldo existente (saldoAnt), duração da chamada (durChama), valor da chamada (valChama), valor do imposto (valImp), valor total da chamada (valTChama), saldo atual (saldoAtual)
custoMin = 1.55
imposto = 18.5 # 18.5%

# Bibliotecas
import math

# Algoritmo
# Passo 1: leia o valor dos créditos e da chamada
saldoAnt = float(input('Qual é o crédito pré-existente? R$ '))
durChama = float(input('Qual foi a duração da chamada? '))
# Passo 2: compute as saídas
# Passo 2.1: calcule o minuto cheio
durChama = math.ceil(durChama)
# Passo 2.2: calcule o valor da chamada sem impostos
valChama = durChama * custoMin
# Passo 2.3: calcule o valor dos impostos
valImp = (valChama * imposto)/100
# Passo 2.4: o total da chamada
valTChama = valChama + valImp
# Passo 2.5: calcule o saldo atual arredondado
saldoAtual = saldoAnt - valTChama
arredondando = int(100 * saldoAtual + 0.5)
saldoAtual = arredondando/100
# Passo 3: imprima os resultados
print('Valor dos Créditos:      R$ {0:7.2f}\n'
      'Valor da Chamada:        R$ {1:7.2f}\n'
      'Valor dos Impostos:      R$ {2:7.2f}\n'
      'Valor total da chamada:  R$ {3:7.2f}\n'
      'Valor do saldo atual:    R$ {4:7.2f}\n'.format(saldoAnt, valChama, valImp, valTChama, saldoAtual))
# Fim do algoritmo
