#------------------//^.^// -------------------#

def remove_aspas_duplas(valor):
    return valor.strip('"')


# Criando o dicionário de atores
atores = {}

# Abrindo o dataset e extraindo os dados
with open('actors.csv', 'r') as arquivo:
    
    # Recolhe as chaves pelo cabeçalho e armazena em atores
    linhas = arquivo.readlines()
    chaves = linhas[0].strip().split(',')
    atores = dict.fromkeys(chaves)
    #print(chaves)
    #print(atores)

    for registro in linhas[1:]:
        
        # Verifique se a string começa e termina com aspas duplas
        if valor.startswith('"') and valor.endswith('"'):
            # Remova as aspas duplas
            valor = valor[1:-1]
        
        # Armazene o valor
        valores = registro.strip().split(',')

        # Remova as aspas duplas dos valores usando a função
        valores = [remove_aspas_duplas(valor) for valor in valores]
        
        # Preencha o dicionário de atores com os valores correspondentes
        for i, chave in enumerate(chaves):
            atores[chave] = valores[i]


    print(atores)


## Se o arquivo tiver sido fechado sem erros, imprima:
if arquivo.closed:
    print('\nExtração concluída com sucesso.')
    print('\n')
    
    for _ in atores:
        print(atores['nome'])




# -------------------------------------------
## Etapa 01: Apresente o ator/atriz com o maior número de filmes e a respectiva quantidade.

# Abrindo a saida
with open('etapa-1.txt', 'w') as saida_1:
    
    print(atores['num_filmes'])
    ## Maior número de filmes
    maior_num_filmes = max(atores['num_filmes'])
    print('\n', maior_num_filmes)

    ## Nome do ator/atriz correspondente
    indice_01 = atores['num_filmes'].index(maior_num_filmes)
    print('\n', indice_01)

    nome_01 = atores['nome'][indice_01]
    print('\n', nome_01)


    # Resultado 01
    etapa_01 = [nome_01, maior_num_filmes]

    # Escreva a saída
    #print('Actor: {} \nQuantidade de filmes: {}\n'.format(*etapa_01, file=saida_1))

## Se o arquivo de saída tiver sido fechado sem erros, imprima:
if saida_1.closed:
    print('\n{} fechado com sucesso! | //^.^// '.format(saida_1.name))
    print('\n', etapa_01)




# -------------------------------------------
## Etapa 02: Apresente a média de receita de bilheteria bruta dos principais filmes `#1 Movie`, considerando todos os atores. Estamos falando aqui da média da coluna `Gross`.

with open('etapa-2.txt', 'w') as saida_2:
    
    print(type(atores['fat_bruto_filme']))

    ## Média de faturamento bruto por ator
    media_fat_bruto_filme = sum(atores['fat_bruto_filme'])/ len(atores['fat_bruto_filme'])

    # Resultado 02
    etapa_02 = media_fat_bruto_filme

    # Escreva a saída
    #print('Média: {}'.format(etapa_02), file=saida_2)

## Se o arquivo de saída tiver sido fechado sem erros, imprima:
if saida_2.closed:
    print('\{} fechado com sucesso! | //^.^// '.format(saida_2))



# -------------------------------------------
## Etapa 03: Apresente o ator/atriz com a maior média de receita de bilheteria bruta por filme do conjunto de dados. Considere a coluna `Avarage per Movie` para fins de cálculo.
with open('etapa-3.txt', 'w') as saida_3:
    
    ## Ator/Atriz com a maior media_fat_bruto
    max_media_fat_bruto = max(atores['media_fat_por_filme'])

    # Resultado 02
    etapa_03 = max_media_fat_bruto

    # Escreva a saída
    #print('Média: {}'.format(etapa_03), file=saida_3)

## Se o arquivo de saída tiver sido fechado sem erros, imprima:
if saida_3.closed:
    print('\{} fechado com sucesso! | //^.^// '.format(saida_3))


# -------------------------------------------
## Etapa 04: A coluna `#1 Movie` contém o filme de maior bilheteria em que o ator atuou. Realize (i) a contagem de aparições destes filmes no dataset, (ii) listando-os ordenados pela quantidade de vezes em que estão presentes. Considere a ordem decrescente e, em segundo nível, o nome do  filme.

with open('etapa-4.txt', 'w') as saida_4:

    filmes = []
    tam = len(atores['filme_maior_fat'])

    ## Quantas vezes os filmes aparecem na coluna `#1 Movie`?

    for linha in tam:
        for filme in tam: 
        # Caso encontre um filme com o mesmo nome...
            if linha != filme:
                # ... adicione na lista de filmes distintos
                filmes.append(atores['filme_maior_fat'][filme])
            else:
                repeticoes_filme = filmes.count(atores['filme_maior_fat'][filme])

    # Resultado 04
    etapa_04 = [filme, repeticoes_filme, ]
    ## Ordenação dos filmes
    etapa_04.sort()
        
    # Escreva a saída
    #print('{} - O filme {} aparece {} vez(es) no dataset.'.format(enumerate(etapa_04), *etapa_04), file=saida_4)

## Se o arquivo de saída tiver sido fechado sem erros, imprima:
if saida_4.closed:
    print('\{} fechado com sucesso! | //^.^// '.format(saida_4))



# -------------------------------------------
## Etapa 05: Apresente a lista dos atores ordenada pela receita bruta de bilheteria de seus filmes (coluna Total Gross), em ordem decrescente.

with open('etapa-5.txt', 'w') as saida_5:

    atores_ord = atores['nome'] 

    # Resultado 05
    etapa_05 = atores_ord

    ## Ordenação dos filmes
    etapa_05.sort(key=atores['fat_bruto'])
    
    # Escreva a saída
    #print('{} '.format(enumerate(etapa_05), *etapa_05), file=saida_5)

## Se o arquivo de saída tiver sido fechado sem erros, imprima:
if saida_5.closed:
    print('\{} fechado com sucesso! | //^.^// '.format(saida_5))

