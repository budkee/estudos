# Este programa recebe um número representando a quantidade de segundos e entrega como saída seu valor em horas, minutos e segundos.
# Leitura dos segundos:
totsegundos = int(input(''))
# Cálculo dos segundos:
segundos = totsegundos % 60
# Cálculo dos minutos restantes:
minutos = (totsegundos // 60) % 60
# Cálculo dos minutos finais:
totminutos = totsegundos // 60
# Cálculo das horas:
horas = totminutos // 60

print(horas, minutos, segundos)