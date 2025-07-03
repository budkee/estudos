// Funcão Call e Função Apply
function getPreco(imposto = 0, moeda = 'R$') {
    return `${moeda} ${this.preco * (1 - this.desc) * (1 + imposto)}`
}

const produto = {
    nome: 'Notebook',
    preco: 4503,
    desc: 0.15,
    getPreco
}

global.preco = 20
global.desc = 0.1
console.log(getPreco()) // Chamando diretamente
console.log(produto.getPreco())


const carro = { preco: 4999, desc: 0.20 }
// Call
console.log(getPreco.call(carro))
console.log(getPreco.call(carro, 0.17, '$'))
//Apply
console.log(getPreco.apply(carro))
console.log(getPreco.apply(global, [0.17, '$']))


