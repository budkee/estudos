console.log(module.exports)
// Referências diferentes
console.log(module.exports === this)
console.log(module.exports === exports)
// Atribuindo valores ao objeto de vária formas
this.a = 1
exports.b = 3
module.exports.c = 4
// Alterando a referência para nulo...
exports = null
// .. ou a um novo objeto
exports = {
    nome: 'Maria'
}
// Não altera o objeto de exportação
console.log(module.exports)

// Para alterar você deve
module.exports = {
    publico: true,
    nome: 'Maria'
}