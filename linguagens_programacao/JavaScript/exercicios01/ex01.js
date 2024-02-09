// Exercício 01 - Função aritmética
function funcaoAritmetica(x, y) {
    soma = x + y
    sub = x - y
    mult = x * y
    div = x/y
    
    return [console.log(`Soma: ${soma}\n`,`Subtração: ${sub}\n`, `Multiplicação: ${mult}\n`, `Divisão: ${div}\n`)]

}

funcaoAritmetica(3,4)