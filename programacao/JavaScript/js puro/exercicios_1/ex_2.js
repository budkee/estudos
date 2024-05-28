/*************
 * Exercício 02 - Função para definição do tipo do triângulo
 * Os triângulos podem ser classificados em 3 tipos quanto ao tamanho de seus lados:  
    Equilátero: Os três lados são iguais. 
    Isósceles:  Dois lados iguais. 
    Escaleno: Todos os lados são diferentes.  
 * Crie uma função que recebe os comprimentos dos três lados de um triângulo e retorne sua classificação quanto  ao tamanho de seus lados. (Neste exemplo deve-se abstrair as condições matemáticas de existência de um triângulo).

    */
function classTriangulo(l1, l2, l3) {
  if (l1 == l2 && l1 == l3 && l3 == l2) {
    console.log("Equilátero");
  } else if (
    (l1 == l2 && l2 != l3) ||
    (l2 == l3 && l1 != l3) ||
    (l3 == l1 && l1 != l2)
  ) {
    console.log("Isósceles");
  } else if ((l1 != l2) != l3) {
    console.log("Escaleno");
  }
}

classTriangulo(3, 4, 5);
