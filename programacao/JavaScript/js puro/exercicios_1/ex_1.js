// Exercício 01 - Função aritmética
// Crie uma função que dado dois valores (passados como parâmetros) mostre no console a soma, subtração, multiplicação e divisão desses valores

function funcaoAritmetica(x, y) {
    soma = x + y
    sub = x - y
    mult = x * y
    div = x/y
    
    return [
      console.log(
        `Soma: ${soma}`,
        `\nSubtração: ${sub}`,
        `\nMultiplicação: ${mult}`,
        `\nDivisão: ${div}`
      ),
    ];

}

funcaoAritmetica(3,4)