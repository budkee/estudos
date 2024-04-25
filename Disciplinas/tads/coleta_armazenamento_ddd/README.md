# Desenvolvimento inicial do sistema de coleta de dados climáticos

- [Projeto de software](https://budkee.notion.site/Open-Weather-Map-3b2e4e5a58ec4898ad31f94c178ca2db?pvs=4)

## Objetivo

Criação de um script que realize a coleta e o armazenamento dos dados em um banco de dados relacional.

## Roteiro do script

1. Consumir a API
2. Recolher os dados de interesse a partir das coordenadas geográficas
3. Armazenar em um dicionário
4. Exportar os dados para o MySQL
5. Exportar o arquivo com os dados para o repositório de execução

### Inputs do usuário

    coleta_armazena.py -in -20.459321687776768 -54.568144519354846 -out coleta_armazena.json

### Outputs esperado

- O arquivo em json da coleta;
- Um texto dizendo que os dados foram ou não salvos no MySQL;
