console.log(typeof String)
console.log(typeof Array)
console.log(typeof Object)
// Toda função tem um atributo chamado .prototype

String.prototype.reversor = function() {
    return this.split('').reverse().join('')
}
console.log('Lucca de Oliveira Budke'.reversor())

Array.prototype.primeiro = function() {
    return this[0]
}

console.log([1, 2, 3, 4, 5].primeiro())
console.log(['a', 'b', 'c'].primeiro())

String.prototype.toString = function() {
    return 'Oi'
}

console.log('Lucca de Oliveira Budke'.reversor())