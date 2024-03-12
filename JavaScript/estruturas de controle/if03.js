const imprimirResultado = function(nota) {
    if (nota >= 7) {
        console.log('Aprovado!')
    } else {
        console.log('Reprovado.')
    }
}

imprimirResultado(10)
imprimirResultado(4)
imprimirResultado('Epa!') // Como o resultado da condição fica como False, ele imprime o bloco de else.

