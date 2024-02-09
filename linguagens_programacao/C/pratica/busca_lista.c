#include <stdio.h>
#define MAX 11


// Funções
int buscaListaEstatica(int *lista, int *valor, int i) {

    // Caso fundamental: se o índice for maior ou igual ao tamanho máximo do vetor.
    if (i >= MAX)
    {
        return -1; // Valor não encontrado

    }
    // Caso ordinário: se o índice for igual ao valor procurado.
    if (lista[i] == &valor) {
        return i; // Retorna o índice
    } else {
        return buscaListaEstatica(lista, &valor, i++); // Verifica o próximo
    }

} 


// Programa: Busca em lista estática 
int main(void) {

    int valor = 0;
    int lista[MAX] = {2, 3, 4, 9, 10, 2, 44, 8, 11, 29};
    printf("Qual é o valor de interesse?\n");
    scanf("%d", &valor);

    int resultado = buscaListaEstatica(lista, valor, 0);

    if (resultado != -1) {
        
        printf("Índice da lista: %d", resultado);

    } else {
        printf("Valor não encontrado.");
    }

    return 0;
}
