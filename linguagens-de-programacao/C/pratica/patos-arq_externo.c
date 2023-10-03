#include <stdio.h>

// Definição da estrutura (struct) para representar os patos
typedef struct {
    int celular;
    int acertos;
} Patos;

int main() {
    // Abra o arquivo externo para leitura
    FILE *arquivo = fopen("patos.txt", "r");

    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return 1;
    }

    // Declarando um array de patos para armazenar os dados lidos
    Patos patos[5];

    // Ler os dados dos patos do arquivo
    for (int i = 0; i < 5; i++) {
        if (fscanf(arquivo, "%d%d", &patos[i].celular, &patos[i].acertos) != 2) {
            printf("Erro ao ler os dados do pato %d\n", i + 1);
            break;
        }
    }

    // Fechar o arquivo
    fclose(arquivo);

    // Imprimir os dados dos patos
    for (int i = 0; i < 5; i++) {
        printf("Pato %d: Celular: %d, Acertos: %d\n", i + 1, patos[i].celular, patos[i].acertos);
    }

    return 0;
}

