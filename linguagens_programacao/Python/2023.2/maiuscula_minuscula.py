def transforma_maiuscula_para_minuscula(frase):
    # Divide a frase em palavras
    palavras = frase.split()

    # Transforma a primeira letra de cada palavra em minúscula, mantendo o restante em maiúscula
    palavras_transformadas = [palavra.capitalize() if len(palavra) > 0 else '' for palavra in palavras]

    # Une as palavras transformadas em uma nova frase
    nova_frase = ' '.join(palavras_transformadas)

    return nova_frase

# Exemplo de uso
frase_original = input("Insira a frase em Maiúscula: ")
frase_transformada = transforma_maiuscula_para_minuscula(frase_original)

print("Frase Original:", frase_original)
print("Frase Transformada:", frase_transformada)
