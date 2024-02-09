/**************************************************
*
* Kaê(Camila) de Oliveira Budke
* Trabalho 2
* Professor(a): Diego Padilha Rubert
*
*/

// Bibliotecas
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Definições
#define MAX_VEICULOS 5
#define NUM_PILHAS 3

/* Armazena informacoes de um veiculo estacionado em uma pilha */
typedef struct cel {
    char placa[9];
    struct cel *prox;
} veiculo;

/* Armazena informacoes de uma pilha */
typedef struct {
    int veiculos; /* Quantidade de veiculos estacionados */
    veiculo *topo; /* Topo da pilha */
} pilha;

typedef struct {
    char data[11];
    pilha P[NUM_PILHAS]; /* Armazena as pilhas P0, P1, ..., NUM_PILHAS-1 */
} estacionamento;


// Funções


void inicializaPilha(pilha *p) {
    p->veiculos = 0; /* Aponta para o campo do primeiro veículo */
    p->topo = NULL; /* Aponta para o campo nulo (fim da pilha) */
}


void imprimirPilha(pilha *p, int pilha_num) {
    
    veiculo *atual = p->topo;

    // Imprime o segmento da pilha
    printf("P%d:", pilha_num);

    // Enquanto houver elementos na pilha
    while (atual != NULL) {
        
        // Manda a placa do atual
        printf("%s", atual->placa);
        
        // Se o próximo elemento estiver preenchido
        if (atual->prox != NULL) {
            printf(",");
        }

        // Atualiza o atual e faz tudo de novo
        atual = atual->prox;
    }
    
    printf("\n");
}

// Inserção de pilha
int estacionarVeiculo(estacionamento *estac, char placa[9]) {
    
    // Pilha com o menor número de veiculos
    int min_pilha = 0;
    // Número de veículos da primeira pilha de veículos
    int min_veiculos = estac->P[0].veiculos;

    // Encontre a pilha com menos veículos
    for (int i = 1; i < NUM_PILHAS; i++) {

        // Se o número de veículos for menor que a pilha com o menor num de veiculos
        if (estac->P[i].veiculos < min_veiculos) {

            // Atualiza a pilha com menor quantidade de veículos e o índice da menor pilha
            min_veiculos = estac->P[i].veiculos;
            min_pilha = i;
        }
    }

    // Verifique se a pilha escolhida não está cheia
    if (estac->P[min_pilha].veiculos >= MAX_VEICULOS) {
        return 0; // Estacionamento cheio
    }

    // Estacione o veículo na pilha escolhida
    veiculo *novo_veiculo = (veiculo *)malloc(sizeof(veiculo));
    // Copia a placa ao novo veículo
    strcpy(novo_veiculo->placa, placa);
    // Aponta a seta do novo veículo para o topo da menor pilha do estacionamento
    novo_veiculo->prox = estac->P[min_pilha].topo;
    
    // Atualiza o topo da menor pilha o valor do novo veículo 
    estac->P[min_pilha].topo = novo_veiculo;
    // Atualiza a quantidade de veículos
    estac->P[min_pilha].veiculos++;

    return min_pilha + 1; // Retorna o número da pilha estacionada
}

int removerVeiculo(estacionamento *estac, char placa[9]) {
    
    // Veículo a ser removido
    int pilha_num = -1;

    // Procure a pilha que contém o veículo de interesse
    for (int i = 0; i < NUM_PILHAS; i++) {
        
        // Inicializa um ponteiro que recebe o endereço do topo e um auxiliar de busca apontando para o vazio
        veiculo *atual = estac->P[i].topo;
        veiculo *aux = NULL;

        // Enquanto houver veículos na pilha atual
        while (atual != NULL) {

            // Verifica se a placa do atual é a mesma de busca
            if (strcmp(atual->placa, placa) == 0) {
                pilha_num = i;
                break;
            }

            // Passa o auxiliar para o atual
            aux = atual;
            // Atualiza o atual para o próximo elemento
            atual = atual->prox;
        }
        
        // Verifica se encontrou a pilha com o veiculo a ser removido
        if (pilha_num != -1) {
            
            // Remova o veículo da pilha
            if (aux == NULL) {

                // Se o veiculo a ser removido está no topo da pilha, entrega o próximo do atual ao topo da pilha
                estac->P[i].topo = atual->prox;

            } else {
                // Caso contrário, atualiza o próximo do elemento anterior com o endereço do próximo atual 
                aux->prox = atual->prox;
            }

            // Libera a memória do veiculo alocado que foi removido
            free(atual);
            // Diminui a qnt de veiculos
            estac->P[i].veiculos--;

            break;
        }
    }

    return pilha_num + 1; // Retorna o número da pilha do veículo removido
}


// Início do programa
int main(void) {

    int num_dias; /* Quantidade de casos de teste*/
    char operacao[2]; /* Criação do vetor */

    // Leitura da 1ra linha
    scanf("%d", &num_dias);

    // Para cada operação...
    for (int i = 0; i < num_dias; i++) {
        
        // Crie o estacionamento
        estacionamento est;

        // Leia o dia da operação
        scanf("%s", est.data);
        printf("%s\n", est.data);

        // Crie a pilha do estacionamento
        for (int j = 0; j < NUM_PILHAS; j++) {
            // Armazena a pilha da vez (?)
            inicializaPilha(&est.P[j]); 
        }

        // Enquanto o usuário estiver ativo...
        while (1) 
        {
            // Leia uma movimentação do estacionamento
            scanf("%s", operacao);

            // Verifica se é a última operação do dia
            if (operacao[0] == 'F') {
                printf("F\n\n");
                break;

              // Verifica se é a entrada (E) de um veículo
            } else if (operacao[0] == 'E') {
                
                char placa[9]; /* Cria uma placa */
                scanf("%s", placa);  /* Lê uma placa */
                int resultado = estacionarVeiculo(&est, placa); /* E */

                // Verifica se está cheio
                if (resultado == 0) {
                    printf("C %s\n", placa);
                } else {
                    // Retorna 
                    printf("E %s\n", est.P[resultado - 1].topo->placa);
                }

              // Verifica se é a saída (S) de um veículo
            } else if (operacao[0] == 'S') {
                
                char placa[9]; /* Cria placa */
                scanf("%s", placa); /* Lê a placa */
                int result = removerVeiculo(&est, placa);
                
                // Verifica qual vai ser o retorno do método
                if (result == 0) {
                    
                    // Caso não exista
                    printf("N %s\n", placa); 
                } else {
                    // Caso exista
                    printf("S %s\n", placa);
                }

              // Verifica se o usuário quer verificar o estado de uma pilha de carros 
            } else if (operacao[0] == 'I') {
                
                int pilha_num; /* Cria uma variável... */
                scanf(" P%d", &pilha_num); /* ... que leia o número da pilha de interesse */

                // Retorna a pilha 
                imprimirPilha(&est.P[pilha_num], pilha_num);
            }

        }
    }
    return 0;
}
