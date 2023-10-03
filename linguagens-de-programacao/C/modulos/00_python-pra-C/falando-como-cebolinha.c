#include <stdio.h>
#include <string.h>

#define MAX_PALAVRA 20

void copiar_cebolinha(char original[], char nova[]) {
    
    int tam = strlen(original);

    for (int i = 0, j = 0; i < tam && j < tam; ) {

        if (original[i] == 'R' && original[i+1] != 'R') {
            
            nova[j] = 'L';
            j++;
            i++;

        } else if (original[i] == 'R' && original[i+1] == 'R') {
            // Diminui o vetor e vá para o próximo indice
            nova[tam-1] = '\0';
            i++;

        } else {
            // PADRÃO
            nova[j] = original[i];
            j++;
            i++;
        }
    }
    // Adiciona o caractere nulo no final da nova string
    nova[tam] = '\0';  
}

int main(void) {
    char palavra[MAX_PALAVRA];
    char palavra_modificada[MAX_PALAVRA];

    scanf("%s", palavra);
    copiar_cebolinha(palavra, palavra_modificada);
    printf("%s\n", palavra_modificada);

    return 0;
}
