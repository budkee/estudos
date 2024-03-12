def inverte(texto):
    inversa = ''
    for letra in texto:
        inversa = letra + inversa

    return inversa


# Leia o texto
# Caracteres maiúsculos e minúsculos são considerados como diferentes.
texto = input()

# Inverta o texto
invertido = inverte(texto)

# Verifique se é palíndromo
if invertido == texto:
    msg = 'palíndromo'
else:
    msg = 'não é palíndromo'

# Imprima o resultado
print(msg)