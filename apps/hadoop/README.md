# Hadoop Log Analysis

## Objetivo

Processar um conjunto de arquivos de log de servidor web Apache e gerar estatísticas, como:

- Quantidade de acessos por IP
- URLs mais acessadas

## Requisitos

- Hadoop instalado (modo pseudo-distribuído ou local)
- JDK (Java)
- Python (opcional, para scripts auxiliares)
- Arquivos de log no formato Apache

### Requisitos de Hardware para Execução Local do Hadoop (modo pseudo-distribuído)

| Recurso | Mínimo Funcional | Recomendado para Fluidez |
| --- | --- | --- |
| CPU | 2 núcleos | 4 núcleos (ou mais) |
| RAM | 4 GB | 8 GB |
| Disco | 10 GB livre | 20 GB+ (com HDFS) |
| Sistema Operacional | Linux (Ubuntu/Debian), macOS, WSL (no Windows) | Linux nativo preferencial |

#### Observações

- 4 GB de RAM é o mínimo absoluto. O Hadoop consome memória (NameNode, ResourceManager, etc.), além do próprio sistema operacional. Com 8 GB, você terá mais margem para testes maiores.

- O projeto de análise de logs que propusemos consome pouco CPU e memória.

- Se você for trabalhar com arquivos de log maiores (acima de 1 GB), o uso de memória pode aumentar um pouco, especialmente na fase de shuffle do MapReduce.

- Para este projeto foi utilizado a ferramenta `multipass` subindo a VM com o seguinte comando:

``` zsh
    multipass launch -n hadoop-log-analysis -c 4 -d 20G -m 8G
```

## Estrutura do Projeto

``` bash
    hadoop-log-analysis/
├── input/
│   └── access_log.txt       # Arquivo de log de entrada
├── mapper.py                # Script Mapper
├── reducer.py               # Script Reducer
├── run.sh                   # Script para rodar o job
└── README.md                # Instruções do projeto

```

### Exemplo de linha de Log (Apache)

``` bash
    127.0.0.1 - - [25/Jun/2025:10:05:23 -0300] "GET /index.html HTTP/1.1" 200 2326
```

## Conceitos Hadoop Utilizados

- HDFS (armazenamento dos logs)
- MapReduce (extração de informações úteis)
- Job Tracker / Task Tracker (mesmo em modo pseudo-distribuído)

## Resultados Esperados

``` bash
    127.0.0.1    24
    /index.html  15
    /about.html  3
```

## Extensões possíveis

- Contar códigos de status HTTP
- Contar acessos por hora ou dia
- Visualizar os resultados em gráficos (com Python + Matplotlib)
