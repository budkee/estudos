#include <stdio.h>
 
int main() {
 
    // Declaracao
    int N[20];
    
    // Leitura
    for (int i = 0; i < 20; i++) {
        scanf("%d", &N[i]);
    }
    
    // Inverte os elementos
    for (int i = 0; i < 10; i++){
        int temp = N[i];
        N[i] = N[19 - i];
        N[19 - i] = temp;
    }
    
    // Vetor modificado
    for (int i = 0; i < 20; i++) {
        printf("N[%d] = %d\n", i, N[i]);
    }
    
 
    return 0;
}