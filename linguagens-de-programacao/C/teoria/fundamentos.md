[![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white)]()

# Fundamentos

## Sumário

### Básico

- [Sintaxe](#sintaxe)
- [Declaração de Variáveis](#declaração-de-variáveis)
- [Operadores](#operadores)
- [Leitura da entrada](#leitura-da-entrada)
- [Comparações](#comparações)
- [Formatação de saída](#formatação-de-saída)
- [Execução](#como-executar-um-programa-em-c)

### Avançado

- [Funções](#funções)
--- 

## Acesso Ágil

> - [Tipos em C](https://www.inf.pucrs.br/~pinho/LaproI/IntroC/IntroC.htm#:~:text=c%20recebe%2011-,Tipos%20de%20Vari%C3%A1veis,-Todas%20as%20vari%C3%A1veis)

> - [Declaração em C](https://www.inf.pucrs.br/~pinho/LaproI/IntroC/IntroC.htm#:~:text=Declara%C3%A7%C3%A3o%20de%20Vari%C3%A1veis)
> - [Inicialização da variável](https://www.inf.pucrs.br/~pinho/LaproI/IntroC/IntroC.htm#:~:text=Inicializa%C3%A7%C3%A3o%20de%20Vari%C3%A1veis%20na%20Declara%C3%A7%C3%A3o)
>



## Sintaxe 
>
> O início de todo programa em C se dá pela seguinte estrutura: 
>
>     #include <stdio.h>
> 
>     int main() {
>         /* seus comandos ficarão aqui! */
>     }
> 
- `*variavel`: ponteiro da variável;

- `#include <stdio.h>`: serve para 


## Declaração de Variáveis
>
> Antes do compilador ler o código do arquivo, é necessário fornecer todos os tipos das variáveis que serão utilizadas no topo do arquivo.
> 
>     double x;
>     int n;
> 

---

## Operadores

### Operadores Aritméticos

- [Tipos em C](https://www.inf.pucrs.br/~pinho/LaproI/IntroC/IntroC.htm#:~:text=c%20recebe%2011-,Tipos%20de%20Vari%C3%A1veis,-Todas%20as%20vari%C3%A1veis)



---

## Leitura da entrada

- `scanf()`: método para receber a entrada

### Strings ou Caracteres
`scanf("%s", palavra)`

`scanf("%c", &caractere)`
    > Reconhece e lê os espaços em branco do usuário;
`scanf(" %c", &caractere)`
    > Pula todos os espaços em branco do usuário, inclusive quebra de linha `\n`, até encontrar um caracter;

### Números Inteiros
`scanf("%d", numero_inteiro)`
    > Pula todos os espaços em branco que encontrar até encontrar um número inteiro.

### Números Reais
`scanf("%f", numero_real)`

---

## Comparações 

### Palavras

- `strcmp(string1, string2)`: compara as duas strings e verifica a ordem alfabética  
- `strncmp`:
- `strcat(destino, origem)`: concatena a palavra de origem com a palavra de destino


---

## Formatação de saída

- `printf()`: método para imprimir a saída

### Palavras ou Strings
`printf("%s", palavra)`
`printf("%c", caractere)`

### Números Inteiros
`printf("%d", numero_inteiro)`

### Números Reais
`printf("%f", numero_real)`


### Espaço em branco
>
> Em linguagens interpretadas, o código indentado é fundamental para compreensão do interpretador em questão. 
>
> > Fragmento em Python
>
>     for i in range(0,10):
>         print(i)
>
> Para o compilador, entretanto, um código indentado, e, um código sem espaçamento entre os comandos, dá no mesmo.
> > **Fragmento em C | Espaçado**
> 
>     int i;
> 
>     for (i = 0; i < 10; i++) {
>         printf(i);
>     }
>
> > **Fragmento em C | Não Espaçado**
>
>     for(i = 0;i < 10;i++){printf(i);}
> 
> > Em suma...
> 
> - O espaço em branco é utilizado para separar palavras de modo a diferenciar variáveis ou funções (`int main` != `intmain`) 


## Funções
>
> Para definir uma função em C, você deve primeiro declarar o tipo de retorno (`int`, `double`, ...), seguido do nome da função e dos parâmetros a serem passados, entre parênteses:
>
>     double expon(double b, int e) {
>         if (e == 0) {
>             return 1.0;
>         } else {
>             return b * expon(b, e - 1);
>         }
>     }
> 

## Execução 

### Como executar um programa em C?
> 
> Existem diversas maneiras de executar um programa em C, mas podemos dividi-las em dois principais contextos:
> 
> - Via IDEs em núvem;
> - Via IDEs locais;
> 
> ## IDES em núvem
>
> - Ao optar por utilizar uma plataforma em Cloud para executar o programa que você construiu, não é necessário realizar instalações locais do compilador. Tudo que você precisa é do código e de uma conta para aquela plataforma.
> - As mais comuns são:
> > - [Repl.it](https://replit.com/~)
> > - [GeeksForGeeks | IDE](https://ide.geeksforgeeks.org/)
> > - [JDoodle](https://www.jdoodle.com/c-online-compiler/)
> > - [Cloud9]() 
> > - [Ideone](https://www.ideone.com/)
> > - [OnlineGBD](https://www.onlinegdb.com/)
> 
> ## IDE locais
> 
> 