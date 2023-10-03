/*************************************
*
* Camila de Oliveira Budke
* Trabalho 1
* Professor(a): Diego Padilha Rubert
*
*/

/**************Registro****************/

typedef struct {

    int numero; /* Número da capivara = posição na largada */
    int num_ultrapassagens; /* Quantidade de ultrapassagens feitas */
    
} capivara;

/**************Bibliotecas****************/
#include <stdio.h>

/***************Funções***************/
    
void troca(int *a, int *b) {
    
    int aux;
    aux = *a; 
    *a = *b; 
    *b = aux; 
    
}


void ordenaPontuacao(int n, capivara v[]) {
    
    int maior;

    for (int i = 0; i < n - 1; i++) {
        
        maior = i;
        
        for (int j = n - 1; j > i; j--) {
            
            if (v[j].num_ultrapassagens > v[maior].num_ultrapassagens){
                
                maior = j;

            } else {
                
                troca(&v[i].num_ultrapassagens, &v[maior].num_ultrapassagens);
            
            };        
        
        };
    };
} 

int verificaEmpate(int n, capivara v[]) {

    for (int i = 0; i < n; i++) {
        
        for (int j = i + 1; j < n; j++) {
            
            // Verifique se há empate 
            if (v[i].num_ultrapassagens == v[j].num_ultrapassagens) {
                printf("\nPato %d: %d \n", pato[i].id, pato[i].pontos);
                printf("Pato %d: %d \n", pato[j].id, pato[j].pontos);
        
                // Verifique o competidor com a menor posição inicial
                if (v[i].numero < v[j].numero) {
                    
                    // Acrescente um ponto
                    v[i].num_ultrapassagens ++;
                    return verificaEmpate();
                    // printf("\nPato %d: %d \n", pato[i].id, pato[i].pontos);
                    // printf("Pato %d: %d \n", pato[j].id, pato[j].pontos);
                    
                };
            
            };
            
        };
    
    };
} 


/************** Início ****************/
int main(void) {
    
    /***********Declarações_Inicializações**************/
    int n, num_ultrapassagem;
    
    /************Entradas****************
    *
    *   Objetivo: deixar ambos com os mesmos índices.
    *
    */
    // Leitura n
    scanf("%d", &n);
    
    // Cria e lê o vetor 
    capivara competidoras[n];

    // Atribuição dos numeros das competidoras
    for (int i = 0; i < n; i++) {
        
        competidoras[i].numero = i + 1;
        competidoras[i].num_ultrapassagens = 0;
        
    }

    while (scanf("%d", &num_ultrapassagem) != EOF)
    {
        for (int i = 0; i < n; i++) {
            
            if (num_ultrapassagem == competidoras[i].numero) {
            // Aplica a regra da competição
                
                // Registro das ultrapassagens
                for (int j = i - 1; j < i; j++) {
                    
                    //printf("\nCompetidora %d ultrapassou o competidora %d\n", competidoras[i].numero, competidoras[j].numero);
                    
                    //printf("\n");

                    // Troca a posiçao
                    troca(&competidoras[i].numero, &competidoras[j].numero);
                    
                    // Pontuação
                    competidoras[i].num_ultrapassagens ++;
                    
                    troca(&competidoras[i].num_ultrapassagens, &competidoras[j].num_ultrapassagens);

                    // Nova fila de patos
                    /*for (int i = 0; i < n; i++)  {
                        printf("%d ", competidoras[i].numero);
                    };

                    printf("\n");

                    // Nova pontuação
                    for (int i = 0; i < n; i++)  {
                        printf("%d ", competidoras[i].num_ultrapassagens);
                    };*/

                    //printf("\n");

                    // Atualiza a posição do passador 
                    //i = j;
                };
                
            };

        };
    };
    
    printf("\n");

    /************Saídas****************
    *    
    *   Objetivo: 
    *   [X] imprimir primeiro a ordem de chegada; 
    *   [ ] ordenar o vetor da classificação de competidoras: verificar por pontos e aplicar as trocas por número.
    *   [ ] imprimir a ordem com a classificação final.
    * 
    */

    // Ordem de Chegada
    for (int i = 0; i < n; i++) {
        
        printf("%d ", competidoras[i].numero);

    }

    printf("\n");

    // Ordenação: modifica o vetor original
    //ordenaClassificacao(n, competidoras);
    //printf("\n");
    // Condição de desempate
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            verificaEmpate(n, competidoras);
        }
    }

    // Classificação
    for (int i = 0; i < n; i++) {
        
        printf("%d ", competidoras[i].numero);

    }
    printf("\n");

    return 0;
}

/**************Fim****************/
