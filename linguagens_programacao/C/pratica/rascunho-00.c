#include <stdio.h>

// Declarações
typedef struct {

    int numero;
    int num_ultrapassagem;

} capivara;

// Funções
void criaFila(int n) {
    
    capivara fila[n];

    for (int i = 0; i < n; i++) {
        fila[i].numero = i + 1;
        // Teste
        printf("%d", fila[i].numero);
    }
}

// Início

int main(void) {
    
    int m, n;

    while (scanf("%d\n%d", &m, &n) != EOF) {
        int soma = m + n;
        printf("Soma: %d\n", soma);
    }

    return 0;
}

// Fim

/*


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

*/
