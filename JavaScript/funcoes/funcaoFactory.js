// Factory simples
function criarPessoa () {
    return {
        nome: "Ana",
        sobrenome: 'Silva'
    }
}

console.log(criarPessoa())

// Factory com parâmetros

function criarProduto(nome, preco, desconto = 0.1) {
    return {
        nome,
        preco,
        desconto,
    }
}


console.log(criarProduto('banana', 40))
console.log(criarProduto('maça', 50))
