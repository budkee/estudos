#include <stdio.h>

/*
  Lê nomes, notas e presenças de cada aluno, e então
  a quantidade de aulas. Adiciona um bônus de 10%
  para quem assistiu pelo menos metade das aulas,
  e escreve o relatório final.
  
  Exemplo de entrada:
3
Fulano
8.5 7
Ciclano
6.0 2
Beltrano
7.0 4
9

  Exemplo de entrada com comentários meus (não dá pra usar no programa):
3        ->  n
Fulano   -> nome aluno 1
8.5 7    -> nota e nº de presenças do aluno 1
Ciclano  -> aluno 2
6.0 2
Beltrano -> aluno 3
7.0 4
9        -> número de aulas do semestre

  Exemplo de saída:
Fulano (7): 9.4
Ciclano (2): 6.0
Beltrano (4): 7.0

*/


#define MAX_NOME 20

int main(void) {
  // Lê a quantidade de alunos
  int n;
  scanf("%d", &n);

  // Cria e lê vetores (nomes, notas, presencas)
  char nomes[n][MAX_NOME+1];
  float notas[n];
  int presencas[n];

  for (int i = 0; i < n; i++)
    scanf("%s%f%d", nomes[i], &notas[i], &presencas[i]);

  // Lê quantidade de aulas
  int aulas;
  scanf("%d", &aulas);

  // Adiciona bônus
  for (int i = 0; i < n; i++)
    if (presencas[i] >= aulas / 2.0)
      notas[i] *= 1.1;

  // Escreve relatório
  for (int i = 0; i < n; i++)
    printf("%s (%d): %.1f\n", nomes[i], presencas[i], notas[i]);
    
  return 0;
}
