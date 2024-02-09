Array.prototype.reduce2 = function(callback, valorInicial) {
    const indiceInicial = valorInicial ? 0 : 1
    let acumulador = valorInicial || this[0]
    for (let i=1; i < this.length; i++) {
        acumulador = callback(acumulador, this[i], i, this)
    } return acumulador
}

const usuarios = [
    { 
        nome: 'Paulo', 
        idade: 45, 
        ativo: false 
    },
    {
        nome: 'Lucca',
        idade: 33,
        ativo: false
    },
    {
        nome: 'Bruna',
        idade: 31,
        ativo: true
    }
]
const soma = (resultado, valor) => resultado + valor
const resultado = usuarios.map(u => u.idade).reduce2(soma)
console.log(resultado)