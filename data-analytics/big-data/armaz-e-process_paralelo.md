# Armazenamento e processamento paralelo

## Cluster de computadores

Um cluster de computadores é um
conjunto de servidores com um mesmo
propósito visando fornecer um tipo de
serviço, como armazenamento ou
processamento de dados.

## Armazenamento paralelo

O armazenamento paralelo consiste em
distribuir e armazenamento de dados através
de diversos servidores (computadores), o que
permite aumentar de forma considerável a
capacidade de armazenamento usando
hardware de baixo custo.

## Appache Hadoop

Gerenciamos esse armazenamento pelo  hadoop  file system (HDFS) ou seja um sistema de arquivos distribuidos.

Entre algumas opções, o Apache Hadoop HDFS
(Hadoop Distributed File System) tem se mostrado
a solução ideal para gerenciar o armazenamento
distribuído em um cluster de computadores.

O HDFS é o software responsável pela gestão do
cluster de computadores definindo como os
arquivos serão distribuídos através do cluster.

Com o HDFS podemos construir um Data Lake que
roda sobre um cluster de computadores e permite
o armazenamento de grandes volumes de dados
com hardware commodity (de baixo custo).

### Como funciona ?

Ao usar um framework de processamento
paralelo, as sub-tarefas são levadas para o
processador da máquina do cluster onde os
dados estão armazenados, aumentando assim a
velocidade de processamento de grandes
volumes de dados.

O HDFS é um servico rodando em todas as
máquinas do cluster, sendo um NameNode
para gerenciar o cluster e os DataNodes
que fazem o trabalho de armazenamento
propriamente dito.

O MapReduce também é um serviçoADAS
