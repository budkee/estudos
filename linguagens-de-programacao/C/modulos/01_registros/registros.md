# Registros | Variável Composta Heterogênea

## Introdução

Podemos agrupar dados de duas formas, através de `variáveis compostas homogêneas` ou por `variáveis compostas heterogêneas`, sendo esta última conhecida também como `registros` ou `estrutura`/`struct`.

## Definição, declaração e uso

Assim, um `registro` é uma estrutura de dados logicamente declarados, composto por seu `identificador` e seus `campos` de declaração, dos quais nos permitem estruturar as variáveis lógicas do nosso código.

### Exemplo | Mercadoria de uma loja

    struct {

        int codigo;
        int quant;
        float valor;
    
    } produto;

### Uso 

De forma genérica podemos representar um registro da seguinte forma:

    struct {

        bloco de declarações;
    
    } identificador;

Também é possível atribuir outras variáveis/identificadores ao mesmo tipo de registro, como no exemplo abaixo:

    struct {

        int codigo;
        int quant;
        float valor;
    
    } produto, estoque, baixa;

### Atribuição de valores

Para atribuir valores às variáveis contidas no registro da seguinte forma:

    identificador.campo = valor;

Continuando com o exemplo das mercadorias de uma loja, temos:

    produto.codigo = 0001;
    produto.quant = 20;
    produto.valor = 12.5;

Também podemos utilizar as variáveis do registro em qualquer parte do código, referenciando da mesma forma que atribuímos:

    if (produto.quant <= 2) {
        printf("Reposição de estoque\n");
    } else {
        printf("Tudo certo!\n");
    }

## Declaração e inicialização simultâneas

Podemos pensar as regras dos `registros` da mesma forma que pensamos sobre os `vetores`.

### Inicialização dos valores

    struct {
        int codigo;
        int quant;
        float valor;
    } produto = {1, 5, 34.5};

## Operações sobre registros

Com registros podemos atribuir e copiar os valores de forma direta a outros tipos de registros, como no exemplo abaixo:

    // Declarando os registros
    struct {
        char tipo;
        int codigo;
        int quant;
        float valor;
    } mercadoria1, mercadoria2;

    // Atribuido valores à mercadoria 1
    mercadoria1.tipo = 'A';
    mercadoria1.codigo = 10029;
    mercadoria1.quant = 62;
    mercadoria1.valor = 10.32 * TAXA + 0.53;

    // Copiando diretamente os campos e valores da marcadoria 1 para mercadoria 3
    mercadoria2 = mercadoria1;


## Exemplos

### Horário

    #include <stdio.h>

    /* Este programa recebe um horário no formato hh:mm:ss e o atualiza em 1 segundo, mostrando o novo horário na saída */
    
    int main(void) {

        struct {
            int hh;
            int mm;
            int ss;
        } agora, prox;
        
        printf("Informe o horário atual (hh:mm:ss): ");
        
        scanf("%d:%d:%d", &agora.hh, &agora.mm, &agora.ss);

        prox = agora;
        
        prox.ss = prox.ss + 1;
        
        if (prox.ss == 60) {
            prox.ss = 0;
            prox.mm = prox.mm + 1;
            
            if (prox.mm == 60) {
                prox.mm = 0;
                prox.hh = prox.hh + 1;
                    
                if (prox.hh == 24) {
                    prox.hh = 0;
                }
            }
        }

        printf("Próximo horário é %d:%d:%d\n", prox.hh, prox.mm, prox.ss);

        return 0;
    }


## Exercícios

- [Exercício 1 | Próxima data]()
- [Exercício 2 | Tempo decorrido entre dois horários]()
- [Exercício 3 | Número de dias decorrio entre duas datas]()
- [Exercício 6 | Dada uma data, forneça o dia da semana ao usuário]()

## Referências

- [Slide](https://drive.google.com/file/d/1MfumzVOrdBRte6xjWrR0dFaE3k7vSRv4/view?usp=drive_link)
