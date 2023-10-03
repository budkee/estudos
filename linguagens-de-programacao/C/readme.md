[![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white)]()

# Linguagem C

## Sumário

- [Setup](#setup)
- [Fundamentos](fundamentos.md)
- [Compilador vs. Interpretador: qual é a diferença?](compiladores_vs_interpretadores.md)
- [Documentação](https://devdocs.io/c/)
- [Exercícios](exercicios.md)
- [Dúvidas](duvidas.md)
- [Erros](#erros)

---

## Setup

Na sua máquina provavelmente terá um compilador pré-instalado. Basta compilar pela CLI:

    $ gcc -Wall -pedantic -std=c99 arquivo.c -o main -lm

Onde,

- `gcc`: compilar
- `-Wall`: mostrar todos os possíveis avisos ao compilar
- `-pedantic`: aumentar o nível de rigidez
- `-std=c99`: qual é o padrão do compilador
- `arquivo.c`: nome do código em c
- `-o`:
- `main`: nome do executável
- `-lm`: caso o import do math dê errado

Em seguida, você deve executar na linha de comando o excutável criado da seguinte forma:

    $ ./main

---

## Erros

- `Segmentation fault`: é algo que ocorre quando você tenta acessar um endereço de memória proibido. Isso ocorre de várias maneiras, como acessar um ponteiro que não foi alocado, uma passagem errada de parâmetro para uma função.
  - Uma forma bem sutil de ocorrer esse problema é quando você quer passar um ponteiro para um int para uma função que recebe isso como parâmetro e você passa um int. Um ponteiro para int é um endereço que na verdade é um número que pode ser armazenado em um int. E isso implica que o compilador não emitirár erros de compilação, embora na maioria dos compiladores seja emitido um warning.
  - [Entenda o que é segmentation fault](https://freedev.medium.com/entenda-o-que-%C3%A9-segmentation-fault-3b496482c668)

### Linguagens influenciadas por C
