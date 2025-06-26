/***************
*
*   Objetivo: ordenar os valores recebidos em um arquivo.txt com os critérios de (1) primeiro os pares em ordem crescente, (2) depois os ímpares em ordem decrescente.
*   
*   Entrada: a primeira linha contém um número N inteiro positivo representando a quantidade de linhas a seguir.
*   Saída: impressão dos números ordenados, linha por linha, seguindo os critérios de ordenação.
*   
*   Estratégia: 
*   
*       1. Criar um vetor para os números pares e outro para os números ímpares. 
*       2. Ordenar cada vetor de acordo com o critério.
*
*/

// Bibliotecas e definições
#include <stdio.h>
#include <stdlib.h>

/*  Funções     */
void troca(int *a, int *b){

    int temp = *a;
    *a = *b;
    *b = temp;
}

int comparador(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}
int comparadorDesc(const void *a, const void *b) {
    return (*(int *)b - *(int *)a);
}

/*  Programa    */ 
int main(void) {

/* Declarações de variáveis */
    int *numeros; 
    int *pares; // Reserva do endereço de memória n * o tamanho de bytes do tipo int
    int *impares;
    int num_pares = 0;
    int num_impares = 0;
    int i = 0;

    /* Leitura */

    // Número de entradas
    int n;
    scanf("%d", &n);

    // Alocação dinâmica do vetor de números
    numeros = (int *)malloc(n * sizeof(int)); 
    pares = (int *)malloc(n * sizeof(int)); // Reserva do endereço de memória n * o tamanho de bytes do tipo int
    impares = (int *)malloc(n * sizeof(int));

    // Leitura dos valores não ordenados
    while (i < n && scanf("%d", &numeros[i]) != EOF)
    {
        // 1.1 Se for par, armazene em pares[]
        if (numeros[i] % 2 == 0) {

            //*pares = int(*) malloc(*sizeof(int));
            pares[num_pares] = numeros[i];
            num_pares++;
            //printf("%d ", &pares[i]);

            // 1.2 Se for ímpar, armazene em impares[]
        } else {

            impares[num_impares] = numeros[i];
            num_impares++;
            //printf("%d ", &impares[i]);
        
        }
        i++;
    }


/* Implementação da estratégia */

    // 1. Ordene cada vetor de acordo com o seu critério
    // Ordenar os números
    // 1.1 Pares: Crescente
    qsort(pares, num_pares, sizeof(int), comparador);
    // 1.2 Impares: Decrescente
    qsort(impares, num_impares, sizeof(int), comparadorDesc);




/* Saída */

    // Números pares
    for (int i = 0; i < num_pares; i++)
    {
        printf("%d \n", pares[i]);
    }

    // Números ímpares
    for (int i = 0; i < num_impares; i++)
    {
        printf("%d \n", impares[i]);
    }

/*      Fim-Saída     */

/*      Fim Programa     */

    // Libere a memória alocada dinamicamente
    free(numeros);
    free(pares);
    free(impares);

    return 0;
}
