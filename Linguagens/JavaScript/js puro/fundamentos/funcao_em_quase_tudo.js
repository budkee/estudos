// Funções em JS
// --------------------------------------------------------
console.log(typeof Object) // O que é um objeto para o JavaScript?

class Produto {}
console.log(typeof Produto) // O que é um objeto para o JavaScript?

// Exemplos básicos #01
// --------------------------------------------------------
// Funções sem retorno
// (a, b) -> atribuição de parâmetros
function imprimirSoma(a, b) {
    console.log(a + b)
} 

imprimirSoma(2, 3)
imprimirSoma(2) // soma de um valor inteiro + undefined
imprimirSoma(2, 5, 4, 5, 6) // pega apenas os primeiros e ignora o resto
imprimirSoma()

// Função com retorno
function soma(a = 0, b = 1) {
    return a + b
}

console.log(soma(3, 4))
console.log(soma(2))

// Exemplos básicos #02
// --------------------------------------------------------
// Armazenando uma função em uma variável
let imprimirSoma2 = function(c, d) {
    console.log(c + d)
}
// Executando
imprimirSoma2(3, 3)

// Armazenando uma função arrow em uma variável
let soma2 = (a, b) => {
    return a + b
} // Retorno da Função

// executando
console.log(soma2(4, 5))

// Retorno implícito
let subtracao = (a, b) => a - b // Retorno da Função

// executando 
console.log(subtracao(4,5))

// 
const imprimir2 = a => console.log(a)
imprimir2("Legal!")