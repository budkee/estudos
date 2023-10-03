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

void desempate(int n, int *i, int *j, capivara v[]) {

    // Objetivo da função: aplicar pontuações extras àqueles que tiveram pontos iguais após o término da corrida.
    // Verifique o competidor com a menor posição inicial
    if (v[*i].numero < v[*j].numero) {
    
        if (v[*j].num_ultrapassagens < v[*j + 1].num_ultrapassagens) {
            
            troca(&v[*j].numero, &v[*j + 1].numero);

        } else if (v[*j].num_ultrapassagens == v[*j + 1].num_ultrapassagens) {

            //desempate(n, capivara v[]);
            if (v[*j].numero < v[*j + 1].numero) {

                troca(&v[*j].numero, &v[*j + 1].numero);
            };

        };


    };    

}

void ordenaClassificacao(int n, capivara v[]) {
    
    // Objetivo da função: ordenar a classificação final dos competidores com base em suas pontuações.

    int maior;

    // Percurso de referência
    for (int i = 0; i < n - 1; i++) {
        
        maior = i;

        // Percurso de comparação
        for (int j = n - 1; j > -1; j--) {
        
            // Se for maior que o maior e for maior do que i aponta
            if (v[j].num_ultrapassagens > v[maior].num_ultrapassagens){

                // Atualiza a posição do maior
                maior = j;
                
                // Troca a posição da classificação
                troca(&v[i].numero, &v[maior].numero);
                //desempate(n, &i, &j, v);

            } else if (v[i].num_ultrapassagens > v[j].num_ultrapassagens) {

                // Não é o maior de todos, mas é o maior que o elemento em i
                troca(&v[j].numero, &v[i].numero);
                desempate(n, &i, &j, v);

            } else if (v[j].num_ultrapassagens == v[i].num_ultrapassagens) {
                
                // Realiza o desempate
                desempate(n, &i, &j, v);
                // Retorna o vetor de ultrapassagens atualizado
            
            };        
            // Atualiza a posição
            i = j;
        };
    };
} 


/************** Início ****************/
int main(void) {
    
    /***********Declarações_Inicializações**************/
    int n, num_ultrapassagem;
    
    // Leitura n
    scanf("%d", &n);
    
    // Cria e lê o vetor 
    capivara competidoras[n + 1];

    // Atribuição dos numeros das competidoras
    for (int i = 0; i < n; i++) {
        
        competidoras[i].numero = i + 1;
        competidoras[i].num_ultrapassagens = 0;
        
    }

    /************Entradas****************/
    while (scanf("%d", &num_ultrapassagem) != EOF)
    {
        for (int i = 0; i < n; i++) {
            
            if (num_ultrapassagem == competidoras[i].numero) {
            // Aplica a regra da competição
                
                // Registro das ultrapassagens
                for (int j = i - 1; j < i; j++) {
                    
                    printf("\nCompetidora %d ultrapassou o competidora %d\n", competidoras[i].numero, competidoras[j].numero);
                    
                    printf("\n");

                    // Troca a posiçao
                    troca(&competidoras[i].numero, &competidoras[j].numero);
                    
                    // Pontuação
                    competidoras[i].num_ultrapassagens ++;
                    
                    troca(&competidoras[i].num_ultrapassagens, &competidoras[j].num_ultrapassagens);

                    // Nova fila de patos
                    for (int i = 0; i < n; i++)  {
                        printf("%d ", competidoras[i].numero);
                    };

                    printf("\n");

                    // Nova pontuação
                    for (int i = 0; i < n; i++)  {
                        printf("%d ", competidoras[i].num_ultrapassagens);
                    };

                    printf("\n");

                    // Atualiza a posição do passador 
                    i = j;
                };
                
            };

        };
    };
    
    printf("\n");

    /************Saídas****************/
    // Ordem de Chegada
    for (int i = 0; i < n; i++) {
        
        printf("%d ", competidoras[i].numero);

    }

    printf("\n");

    /************Ordenação****************/
    ordenaClassificacao(n, competidoras);
    printf("\n");

    // Classificação
    for (int i = 0; i < n; i++) {
        
        printf("%d ", competidoras[i].numero);

    }
    printf("\n");

    return 0;
}

/**************Fim****************/
