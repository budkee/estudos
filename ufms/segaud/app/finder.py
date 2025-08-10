"""
## Entradas    
    - Leitura de parametros pelo terminal
        1. da string, ex.: "Welcome!" 
        2. do arquivo, ex.: SMario.sfc

## Saída Esperada
    
    - Offset (posição na ROM) e Valor Hexdecimal
    
    {"offset": 
        "hexadecimal": "78",
        "ASCII": "x" 
    }
    
    ex.: 00000000: 78
"""
# Imports
import os

# Funções
def run():
    
    try:
        # Leitor
        # 1. da string, ex.: "Welcome!" 

        # 2. do arquivo, ex.: SMario.sfc
        with open() as bi:

            # Mapeador 
            return print("A posição de {palavra} está em {offset} e seu valor em Hexadecimal é {hex10}.")

    except Exception as e:
        print('Algo de errado não está certo: {e}')







# Main
if __name__ == "__main__":
    
    run()


