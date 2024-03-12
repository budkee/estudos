// Serve para mapear os elementos de um array original, gerando um novo array a partir do original.
const nums = [ 1, 2, 3, 4, 5]

// Função map é um laço for com propósito definido
let resultado = nums.map(function(e) {
    return e * 2
})

console.log(resultado)

// Criando 3 funções e mapeando elas
const soma10 = e => e + 10
const triplo = e => e * 3
const paraDinheiro = e => `R$ ${parseFloat(e).toFixed(2).replace('.',',')}`

resultado = nums.map(soma10).map(triplo).map(paraDinheiro)
console.log(resultado)