// Içamento da variável: o código joga a variável pra cima.
// Funciona apenas com var.


// var a
console.log('a = ', a) // a = undefined
// a = 2
var a = 2

console.log('a = ', a) // a = 2 

// ------------------------------------------------
// Exemplo de função com var:

function teste() {
    
    // var a
    console.log('a = ', a) // a = undefined
    var a = 2
    console.log('a = ', a) // a = 2 

}
teste()

// ------------------------------------------------

console.log('b =', b) // ReferenceError: b is not defined.
let b = 2
console.log('b =', b) // 

