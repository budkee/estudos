/******************************************

* Nome do(a) estudante: Camila de Oliveira Budke
* Trabalho 1
* Professor(a): Diego Padilha Rubert


--> Sobre a corrida

A corrida começa com n capivaras posicionadas em fila. Cada capivara recebe um número de 1 a n, de acordo com a sua posição na fila.

--> Como ocorre a Pontuação?

A cada ultrapassagem, a capivara ganha 1 ponto. A que tiver mais pontos ganha a corrida.

*   Condição 1: caso duas capivaras terminem com a mesma quantidade de pontos, verifica-se o desempate pela menor posição inicial na fila.

--> Tipo da Entrada: int

* 1ra linha: quantidade de capivaras (n > 0); 
* 2da linha: ultrapassagens (
    
    Ex. de entrada: 4 -> a capivara da posição 4 ultrapassou a capivara 3
); 
 
    * Obs.: a capivara que está na primeira posição nunca fará uma ultrapassagem.
 
--> O que temos que retornar?

- [] A ordem das capivaras no final da corrida;
- [] A classificação de todas as capivaras.
    
 
--> Saida: list

* 1ra linha (lista da chegada): list de int em ordem crescente;
* 2a linha (lista da classificação): list de int em ordem decrescente;


/**************Registros****************/
typedef struct {

    int numero; /* Número da capivara = posição na largada */
    int num_ultrapassagens; /* Quantidade de ultrapassagens feitas */
    
} capivara;


/***************Funções***************/

void troca(int *a, int *b) {
    
    int aux;
    aux = *a; 
    *a = *b; 
    *b = aux; 
    
};

/**************Bibliotecas****************/
#include <stdio.h>


/************** Início ****************/
int main(void) {

    // Declarações
    int n, num_ultrapassagem;
    capivara competidoras[n+1];
    
    // Leitura primeira linha
    printf("Quantas capivaras inscritas? ");
    scanf("%d", &n);
    
    // Período da corrida
    while (scanf("%d", &num_ultrapassagem) != EOF) {
        
            
        // Leitura da segunda linha em diante
        scanf("%d", &num_ultrapassagem); 

        printf("Capivara %d ultrapassou a capivara %d", &num_ultrapassagem, ++&num_ultrapassagem);   

        // Regra da competição
        if (num_ultrapassagem == competidoras[i].numero) {
        
            // Verifica se a primeira colocada está ultrapassando
            if (competidoras[0].numero == num_ultrapassagem) 
            {

                i++; // Passe para próxima entrada

            } else /* Aplique a regra */ {
                // Troca a posição das competidoras
                troca(&competidoras[i-1], &competidoras[i]);
                // Atribui pontuação
                competidoras[i].num_ultrapassagens += 1;
            };
        }
        
        // Condição de desempate
        if (competidoras[i].num_ultrapassagens == competidoras[j].num_ultrapassagens) {
            // Critério de desempate
            /* Verifica se posição inicial é menor que a atual */
            if (competidoras[i].numero < competidoras[j].numero) {
                // i ganha a posição
            } else {
                // j ganha a posição
            }

        }
    
        if (scanf("%d", &num_ultrapassagem) == EOF) {
            break; // sai da leitura
        }

    }

    // Busca por seleção
    
    for (int j = i+1; j < n; j++){

    }
        
    
    }
    /**************Escritas****************/
    // Chegada
    // 01. [1, 2, 4, 3, 5]
    // 02. []
    // Classificação
    // 01. [4, 2, 1, 3, 5]
    // 02. []

    return 0;
}

/**************Fim****************/