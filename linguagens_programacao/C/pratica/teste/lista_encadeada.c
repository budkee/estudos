#include <stdio.h>
#include <stdlib.h>

// Definição
typedef struct cel {
    int valor;
    struct cel *prox;
} celula;

// Inicialização
// Sem cabeça 
// celula *lista;
// lista = NULL;

// Com cabeça
//celula c, *lista;
//c.prox = NULL;
//lista = &c;

// Imprimir lista
void imprimirLista(celula *lista) {
    
    celula *p;
    
    for (p = lista; p != NULL; p = p->prox) {
        printf("%d\n", p->valor);
    };
}

// Inserção
void inserirLista(celula **lista, int x) 
{
    // Declarar
    celula *nova, *p;
    // Inicializar o espaço
    nova = (celula *) malloc(sizeof (celula));
    p = *lista;
    // Passar o valor a ser inserido à nova celula
    nova->valor = x;
    // Atualiza o fim da nova
    nova->prox = NULL;
    
    // Grazi
    // Caso a lista esteja vazia
    if (*lista == NULL) {
        *lista = nova;
    } else {
        while(p->prox != NULL){
            p = p->prox;
        };
        p->prox = nova;

    }

    // Diego
    //nova->prox = p->prox;

}

// Buscar
celula *buscaLista(celula *lista, int y) 
{
    // Caso o prox esteja apontando para NULL
    if (lista->prox == NULL)
        return NULL;

    if (lista->prox->valor == y)
        return lista->prox;
    
    return buscaLista(lista->prox, y);
}

// Busca e Remoção
void removeLista(celula *p) {
    
    // Declara
    celula *lixo;
    // Inicializa
    lixo = p->prox;
    p->prox = lixo->prox;
    free(lixo);

}

int main(void){

    // Declaração
    celula *lista;
    int valor;

    // Incialização
    lista = (celula *) malloc(sizeof (celula));
    lista->prox = NULL;
    
    // Programa
    while (scanf("%d", &valor) != EOF)
    {
        /* Inserção */
        //scanf("%d", &valor);
        inserirLista(&lista, valor);
        //printf("%d ", lista->valor);
        
        imprimirLista(lista->prox);
        /* Busca */
        //buscaLista(lista, 5);
        
    }
    // Busca

    
    // Impressão
    // Sem cabeça:
    // imprimirLista(lista);
    // Com cabeça:
    //imprimirLista(lista->prox);


    return 0;
}
