"""
    Menu de opções:
    1 - Transformar uma frase TODA MAIÚSCULA em toda minúscula;
    2 - Transformar uma frase TODA MAIÚSCULA em somente a primeira letra Maiúscula e o resto minúscula;
    3 - Transformar uma frase TODA MAIÚSCULA em somente a primeira letra MAIÚSCULA;
    4 - Transformar uma frase toda minúscula em TODA MAIÚSCULA;

"""
import re

def menu_opcao(opcao, frase):
    # 1. Transformar uma frase TODA MAIÚSCULA em toda minúscula;
    if opcao == 1:
        nova_frase = Maiuscula_minuscula(frase, 1)
    
    # 2. Transformar uma frase TODA MAIÚSCULA em Somente a primeira letra maiúscula e o resto minúscula;
    elif opcao == 2:
        nova_frase = Maiuscula_minuscula(frase, 2)
    
    # 3. Transformar uma frase TODA MAIÚSCULA em Todas As Primeira Letras Maiúsculas;
    elif opcao == 3:
        nova_frase = Maiuscula_minuscula(frase, 3)

    # 4. Transformar uma frase toda minúscula em TODA MAIÚSCULA;
    elif opcao == 4:
        nova_frase = minuscula_Maiuscula(frase)
    else:
        nova_frase = "Opção inválida"

    return nova_frase

# Opçoes de 1 a 3
def Maiuscula_minuscula(frase, opcao):
    # Utiliza expressões regulares para dividir a frase em palavras
    palavras = re.findall(r'[.!?]+', frase)

    # Verifica a opção escolhida e transforma a frase conforme o resultado.
    # 1. Transforma toda a frase em minúscula;
    if opcao == 1:
        nova_palavra = [palavra.lower() if palavra.strip() else ' ' for palavra in palavras]
    
    # 2. Transforma Somente a primeira letra maiúscula e mantém o resto da palavra minúscula;
    elif opcao == 2:
        nova_palavra = [palavra.capitalize() for palavra in palavras]
    
    # 3. Transforma Todas As Primeira Letras Em Maiúsculas;
    elif opcao == 3:
        nova_palavra = [palavra.title() for palavra in palavras]

    # Une as palavras transformadas em uma nova frase
    nova_frase = ''.join(nova_palavra)

    return nova_frase


def minuscula_Maiuscula(frase):
    # Utiliza expressões regulares para dividir a frase em palavras
    palavras = re.findall(r'[.!?]+', frase)

    # Transforma toda a frase em Maiúscula;
    nova_palavra = [palavra.upper() if palavra.strip() else ' ' for palavra in palavras]

    # Une as palavras transformadas em uma nova frase
    nova_frase = ''.join(nova_palavra)

    return nova_frase


# Módulo principal
if __name__ == '__main__':

    # Menu de opções
    print("Qual é a formatação que você quer? ")
    print("[1] De MAIÚSCULA -> todas as letras minúsculas")
    print("[2] De MAIÚSCULA -> Somente a primeira letra da frase maiúscula")
    print("[3] De MAIÚSCULA -> Todas As Primeiras Letras Maiúsculas")
    print("[4] De minúscula -> TODAS AS LETRAS MAIÚSCULAS")

    # Recebe a opção do usuário, a frase e chama a função menu_opcao.
    opcao = int(input("Opção: "))
    frase = input("Insira a frase: ")
    nova_frase = menu_opcao(opcao, frase)

    # Imprime a frase transformada.
    print("Frase Transformada:", nova_frase)

"""
    Referência
    - https://www.w3schools.com/python/python_ref_string.asp
"""