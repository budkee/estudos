# Diretório com Arquivos .exs

Este diretório contém arquivos com extensão ".exs" e contêm scripts de Elixir. Eles são projetados para serem executados diretamente sem a necessidade de compilação prévia. Isso é útil para scripts simples, testes rápidos, tarefas de automação e outras operações em que você deseja executar o código sem a sobrecarga de compilar.

## Como Executar de modo local

### 1. Pré-requisitos

- Certifique-se de ter o Elixir instalado em sua máquina. Caso contrário, siga as instruções de instalação em: https://elixir-lang.org/install.html

### 2. Compilação e Execução

1. Abra o terminal e navegue até este diretório.
2. Para compilar os arquivos ".exs", utilize o seguinte comando:

    elixir nome_do_arquivo.exs

Isso é tudo! Agora você pode executar os arquivos ".exs" neste diretório.

## Como Executar com Docker

Se preferir executar os arquivos ".exs" em um ambiente Dockerizado, siga os passos abaixo:

### 1. Puxe a imagem

    docker pull elixir

### 2. Execute o container no diretório onde está o arquivo

    docker run -it --rm --name elixir_lab -v "$PWD":/usr/src/lab -w /usr/src/lab elixir elixir nome_do_arquivo.exs
