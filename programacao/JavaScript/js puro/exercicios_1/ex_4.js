/**
 * Exercício 4 - Função da divisão.
 * Crie uma função que irá receber dois valores, o dividendo e o divisor. A função deverá imprimir o resultado e o resto da divisão destes dois valores.
 * @param {dividendo}  
 * @param {divisor}  
 * @returns {quociente, resto}
 */

function Divisao(dividendo, divisor) {
  quoc = dividendo / divisor;
  resto = dividendo % divisor;
  return [quoc, resto];
}
console.log(Divisao(323, 2));
