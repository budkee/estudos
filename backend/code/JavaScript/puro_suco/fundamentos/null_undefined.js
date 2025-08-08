// Atribuição por referência - Trabalho com objetos e funções
// -------------------------------------------------------

const a = {name: 'Teste'} // aponta para [o objeto] um lugar na memória ("a constante 'a' recebe o objeto")
// undefined
// a
// {name: "Teste"}
const b = a // aponta para [a variável 'a'] o lugar da variável 'a' na memória ("a constante 'b' recebe o endereço de 'a'")
// undefinded
b.name = 'Opa'
// "Opa"

// ---------------------------------------------------------

// Cópia do valor - Trabalho com tipos primitivos
// ---------------------------------------------------------
let c = 3
// undefined
let d = c
// undefined
console.log(d++)
console.log('d = ' + d)
console.log('c = ' + c)

// --------------------------------------------------------

// Undefined

let valor  // não inicializada, sem atribuição
console.log(valor)
// undefined
// TypeError
// console.log(valor2)
// it is not defined

// Null

valor = null // ausência de valor | aponta pra ninguém 
console.log(valor)
// console.log(valor.toString())

// --------------------------------------------------------
const produto = {}
console.log(produto.preco)
// undefined
// console.log(produto.preco.a)
console.log(produto)
produto.preco = 3.5
console.log(produto)

produto.preco = undefined // Evitar essa atribuição
console.log(!!produto.preco)
// delete produto.preco
console.log(produto)

produto.preco = null // retira o preço
console.log(!!produto.preco)
console.log(produto)

