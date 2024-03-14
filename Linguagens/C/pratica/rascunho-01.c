#include <stdio.h>

// Declarações
typedef struct {

    int numero;
    int num_ultrapassagem;

} capivara;

// Funções
void criaFila(int *n) {
    
    capivara filaCorrida[*n];
    // numero[i];
    // quant de ultrapassagens[i];

    for (int i = 0; i < *n; i++) {
       
       filaCorrida[i].numero = i + 1;
        // Teste
        printf("%d", filaCorrida[i].numero);
    }
    
    
}

// Início

int main(void) {

    // Declarações
    int n;
    capivara competidoras[n + 1];

    // Leitura por arquivo
    while (scanf("%d", &n) != EOF) {
        
        criaFila(&n);

        return 0;
    }

    //Saída do vetor
    for (int i = 0; i < n; i++) {

        printf("%d", competidoras[i].numero);
    }    
    return 0;
}

// Fim

/*


*/
