/*******************
*
*   Este programa realiza a soma entre duas variáveis lidas através de um arquivo recebido pela linha de comando.
*   É um exemplo de como escrever um programa que tem como fim da leitura de dados o fim do arquivo (EOF).
* 
*/


#include <stdio.h>

int main(void) {
    
    int m, n;

    while (scanf("%d%d", &m, &n) != EOF) {
        int soma = m + n;
        printf("Soma: %d\n", soma);
    }

    return 0;
}
