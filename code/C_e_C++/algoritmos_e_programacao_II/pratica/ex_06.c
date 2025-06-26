// Bibliotecas
#include <stdio.h>
#include <string.h>

// Definições
#define MAX 100

/*  Sobre | Ponteiros e cadeias

    Crie uma função que realize a conversão de letras minúsculas para maiúsculas.

*/
// Funções
void maiuscula(palavra[]) {

    for (int i = 0; palavra[i] != '\0'; i++) {

        if (palavra[i] >= 'a' && palavra[i] <= 'z') {

            palavra[i] -= 'a' - 'A' // ou palavra[i] += 'A' - 'a'
        }

        /* Ou:

        cadeia[i] = toupper(cadeia[i]);
        
        */
    }
};

// Início
int main(void){
    
    // Declarações
    char palavra[MAX];

    // Leitura
    scanf("%s", palavra);
    // Conversão
    maiuscula(palavra);
    // Saída
    printf("%s\n", palavra);

    return 0;
}
// Fim
