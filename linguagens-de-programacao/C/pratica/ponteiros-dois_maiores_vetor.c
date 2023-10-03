#include <stdio.h>
#include <stdlib.h>

void troca(int *a, int *b) {
    
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;  
}


void maior_menor(int n, int v[n]) {

    for (int i=0; i < n; i++) {

        for (int j = n - 1; j > 0; j--) {

            if (v[i] > *maior) {
                *maior = v[i]; // modifica o valor na qual o maior aponta passando o valor do elemento do vetor.
                *menor = v[i]; 
            } else if (v[i] < *menor) {
                *menor = v[i];
            }

            // Caso haja elementos repetidos
            if (v[i] == v[j]){
                printf("%d Elemento repetido.\n", v[j]);
            }

        }
        
        printf("%d ", v[i]);
    }

    
}

int main(void) {

    int n;
    scanf("%d", &n); 
    
    int v[n];

    for (int i = 0; i < n; i++) {
        
        scanf("%d", &v[i]);
        printf("%d ", v[i]);
    
    }
    
    printf("\n");

    int pr = 0, ult = 0;
    maior_menor(n, v, &maior, &menor);
    
    printf("\n");
    printf("O maior elemento é %d e o menor é %d\n", maior, menor);

    return 0;
}
