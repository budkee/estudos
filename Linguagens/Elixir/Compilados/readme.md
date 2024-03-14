# Diretório com Arquivos .ex

Este diretório contém arquivos com extensão ".ex" e contêm código Elixir compilável. Eles são usados para definir módulos, funções, macros e outros elementos que precisam ser compilados antes de serem executados. Quando você tem um arquivo ".ex", você precisa compilá-lo antes de poder executar o código contido nele.

## Como Executar de modo local

### 1. Pré-requisitos

- Certifique-se de ter o Elixir instalado em sua máquina. Caso contrário, siga as instruções de instalação em: https://elixir-lang.org/install.html

### 2. Compilação e Execução

1. Abra o terminal e navegue até este diretório.
2. Para compilar os arquivos ".ex", utilize o seguinte comando:

    mix compile

3. Após a compilação, você pode executar os arquivos compilados usando o seguinte formato:

    mix run -e "NomeDoModulo.funcao(parametros)"

Substitua "NomeDoModulo" pelo nome do módulo e "funcao(parametros)" pela função que deseja executar.

### 3. Exemplo
Por exemplo, para executar a função `hello/0` no módulo `HelloWorld`, você usaria o seguinte comando:

    mix run -e "HelloWorld.hello()"

Isso é tudo! Agora você pode compilar e executar os arquivos ".ex" neste diretório.

## Como Executar com Docker

Se preferir executar os arquivos ".ex" em um ambiente Dockerizado, siga os passos abaixo:

### 1. Puxe a imagem

    docker pull elixir

### 2. Execute o container no diretório onde está o arquivo

    docker run -it --rm --name elixir_lab -v "$PWD":/usr/src/lab -w /usr/src/lab elixir sh -c "elixirc primeiro_ultimo.ex && elixir primeiro_ultimo.ex"

Ou

    docker run -it --rm --name elixir_lab -v "$PWD":/usr/src/lab -w /usr/src/lab elixir sh -c "elixirc primeiro_ultimo.ex"

