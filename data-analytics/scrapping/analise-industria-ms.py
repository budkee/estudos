# Abrir o arquivo
arquivo = open('CEMPRE-MS.csv')

## Tratamento de dados
for registro in arquivo:
    
    linhas = arquivo.readlines()
    cabecalho = linhas[0].strip().split(';')
    
    atividade = cabecalho[1:]
    atividades = []
    for i, valor in enumerate(atividade):
        print(i, valor)
        atividades.append(valor)

    #for coluna in cabecalho[1:]:
    # Criando os registros por listas
    #for linha in linhas[1:]:
        
        #print(*linha.strip().split(';'))
    
## Fechar o arquivo
arquivo.close()
