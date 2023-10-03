#include <stdio.h>

char troca_letra(char *letra) {
  
  char nova_letra;

  switch (*letra)
  
  {
  case 'R':
    nova_letra = 'L';
    break;
  
  default:
    nova_letra = *letra;
    break;
  }

  return nova_letra;

}

void copiar_cebolinha(char original, char nova_palavra) { 
    
    int *i = 0;

    while (original[i] != "\0") {

      nova_palavra[i] = troca_letra(original[i]);

      i++;
    }
  
}