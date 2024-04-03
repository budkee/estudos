# Data Lake (DL)
>
> É um repositório centralizado que permite armazenar dados estruturados e não estruturados em qualquer escala.
> 
> A diferença entre este e o [Data Warehouse]() é que não há uma limpeza e organização dos dados coletados ao armazená-los.
> 
> A limpeza e formatação de dados ocorre após a coleta bruta, momento no qual se alinham os requisitos do negócio com dados coletados, direcionando a análise e relatórios.
> 
## Principal desafio
>
> > O principal desafio ao utilizar esse conceito ocorre ao armazenar dados sem supervisão do tipo de conteúdo. Assim, é necessária a criação de mecanismos para catalogar e proteger os dados, evitando que o Data Lake se transforme em um Data Swamp (Pântano de Dados). 
>
## Pontos importantes
> 
> - É possível importar dados do DW para o DL e vice-versa;
> - Utiliza-se o processo de ELT, pois primeiro se carrega o dado e depois ocorre a transformação;

## Como se cria um Data Lake?
>
> Para se criar um Data Lake, podemos recorrer ao [Apache Hadoop](https://hadoop.apache.org/) ou a um [BD NoSQL](bd-nao-relacional.md).
>
> 

## Benefícios do DL
>
> - Armazenamento em formato bruto;
> - Importação de qualquer quantidade de dados em tempo real;
> - Repositório Central para todos os dados da empresa;
> - Sem necessidade de movimentação dos dados;
>

## Ferramentas | Open Source
> 
> - [Apache Hadoop](https://hadoop.apache.org/)
>