#include <stdio.h>

// Registros
typedef struct {
    
    int id;
    int pontos;

} patos;

// Funções
void troca(int *a, int *b) {
    
    int aux;
    aux = *a; 
    *a = *b; 
    *b = aux; 
    
}

void desempate(int n, patos v[], int *i, int *j) {

    // Objetivo da função: aplicar pontuações extras àqueles que tiveram pontos iguais após o término da corrida.
    
    // Percurso de referência
    for (int k = 0; k < n - 1; k++) {
        
        // Percurso dinâmico
        for (int l = n - 1; l < k; l--) {
        
            // Verifique o competidor com a menor posição inicial
            if (v[*i].id < v[*j].id) {
                
                // Acrescente um ponto
                v[*i].pontos ++;
                
            };
        
        };
    
    };
} 

void ordenaClassificacao(int n, patos v[]) {
    
    // Objetivo da função: ordenar a classificação final dos competidores com base em suas pontuações.

    int maior = n;

    // Percurso de referência
    for (int i = 0; i < n; i++) {
        
        // Percurso de comparação
        for (int j = i - 1; j < i; j++) {
        
            if (v[j].pontos > v[maior].pontos && v[j].pontos > v[i].pontos){

                // Atualiza a posição do maior
                maior = j;
                
                // Troca a posição da classificação
                troca(&v[j].id, &v[i].id);

            } else if (v[j].pontos > v[i].pontos) {

                // Não é o maior de todos, mas é o maior que o elemento de referência
                troca(&v[j].id, &v[i].id);

            } else if (v[j].pontos == v[i].pontos) {
                
                // Realiza o desempate
                desempate(n, v, &i, &j);
                // Retorna o vetor de pontos atualizado
            
            };        
        
        };
    };
} 


// Início
int main(void) {

    // Declarações
    int n, num_ultrapassagem;

    // Saída 1
    printf("Início\n");
    
    // Leitura de n
    scanf("%d ", &n);
    
    // Cria o vetor 
    patos pato[n];

    // Atribuição dos ids
    for (int i = 0; i < n; i++) {
        
        pato[i].id = i + 1;
        pato[i].pontos = 0;
        
        //printf("Número do pato[%d]: %d\n", i, pato[i].id);
    }
    
    printf("\nOrdem dos competidores: " );
    
    // Fila de patos antes
    for (int i = 0; i < n; i++)  {
        printf("%d ", pato[i].id);
    }

    // Leitura das ultrapassagens e aplicação das regras da competição
    while (scanf("%d", &num_ultrapassagem) != EOF) {
        
        for (int i = 0; i < n; i++) {
            
            if (num_ultrapassagem == pato[i].id) {
            // Aplica a regra da competição
                
                // Registro das ultrapassagens
                for (int j = i - 1; j < i; j++) {
                    
                    printf("\nPato %d ultrapassou o pato %d\n", pato[i].id, pato[j].id);
                    
                    printf("\n");

                    // Troca a posiçao
                    troca(&pato[i].id, &pato[j].id);
                    
                    // Pontuação
                    pato[i].pontos ++;
                    
                    troca(&pato[i].pontos, &pato[j].pontos);

                    // Nova fila de patos
                    for (int i = 0; i < n; i++)  {
                        printf("%d ", pato[i].id);
                    };

                    printf("\n");

                    // Nova pontuação
                    for (int i = 0; i < n; i++)  {
                        printf("%d ", pato[i].pontos);
                    };

                    printf("\n");

                    // Atualiza a posição do passador 
                    i = j;
                };
                
            };

        };
        
    };

    // Condição de desempate
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            
            if (pato[i].id == pato[j].id) {
                //verificaEmpate(n, pato);
                ordenaClassificacao(n, pato);
                // Classificação final
                printf("%d ", pato[i].id);
            }
        }
    }
    

    /************Saídas****************/

    // Chegada
    /*for (int i = 0; i < n; i++) {
        
        printf("%d ", pato[i].id);

    }*/
    printf("\n");

    for (int i = 0; i < n; i++) {
        
        //printf("%d ", pato[i].pontos);

        printf("%d ", pato[i].id);

    };
    //ordenaPontuacao(n, pato);
    
    printf("\n");

    // Classificação
    ordenaClassificacao(n, pato);
    
    for (int i = 0; i < n; i++) {
        
        //printf("%d ", pato[i].pontos);

        printf("%d ", pato[i].id);

    };

    return 0;
}
// Fim
