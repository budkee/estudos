#include <stdio.h>
#include <stdbool.h>

#define MAX 51

int main(void) {
    
    int n;

    while (1) {
        
        scanf("%d", &n);

        if (n == 0) {
            break;
        }

        bool fila_descartada[MAX] = {false};
        int sobra = n;
        int index = 0;
        int descartadas[MAX];  // Array para armazenar as cartas descartadas
        int count_descartadas = 0;

        while (sobra > 1) {
            // Descartar a carta do topo
            fila_descartada[index] = true;
            descartadas[count_descartadas++] = index + 1;

            // Encontrar a próxima carta não descartada
            int count = 0;
            while (count < 2) {
                index = (index + 1) % n;
                if (!fila_descartada[index]) {
                    count++;
                }
            }

            sobra--;
        }

        // Imprimir as cartas descartadas
        printf("Discarded cards:");
        for (int i = 0; i < count_descartadas; i++) {
            printf(" %d", descartadas[i]);
            if (i < count_descartadas - 1) {
                printf(",");
            }
        }

        // Encontrar a última carta remanescente
        for (int i = 0; i < n; i++) {
            if (!fila_descartada[i]) {
                printf("\nRemaining card: %d\n", i + 1);
                break;
            }
        }
    }

    return 0;
}
