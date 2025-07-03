#include <stdio.h>

typedef struct {

  int numero;
  int num_ultrapassagens;

} pato;


int main(void) {
  
  // Lê a quantidade de patos
  int n;
  scanf("%d", &n);

  // Cria e lê vetor com todos os patos
  pato nossos_patos[n];
  
  for (int i = 0; i < n; i++)
    //era assim: scanf("%s%f%d", nomes[i], &notas[i], &presencas[i]);  
    scanf("%s%f%d", nossos_patos[i].numero, &meus_alunos[i].nota, &meus_alunos[i].presencas);

  // Lê quantidade de aulas
  int aulas;
  scanf("%d", &aulas);

  // Adiciona bônus
  for (int i = 0; i < n; i++)
    if (meus_alunos[i].presencas >= aulas / 2.0)
      meus_alunos[i].nota *= 1.1;

  // Escreve relatório
  for (int i = 0; i < n; i++)
    printf("%s (%d): %.1f\n", meus_alunos[i].nome, meus_alunos[i].presencas, meus_alunos[i].nota);
    
  return 0;
}

