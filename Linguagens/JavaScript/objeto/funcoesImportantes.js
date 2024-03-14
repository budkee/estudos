const pessoa = {
    nome: 'Rebecca',
    idade: 1,
    peso: 12
}

console.log(Object.keys(pessoa)) // Pega todas as chaves de um objeto.
console.log(Object.values(pessoa)) // Pega todos os valores de um objeto.
console.log(Object.entries(pessoa)) //Pega todas as entradas do objeto.

Object.entries(pessoa).forEach(([chave, valor]) => {
    console.log(`\n`)
    console.log(`${chave}: ${valor}`)
})

Object.defineProperty(pessoa, 'dataNascimento', {
    enumerable: true,
    writable: false,
    value: '01/01/2000'
})

pessoa.dataNascimento = '01/01/1998'
console.log(pessoa.dataNascimento)
console.log(Object.keys(pessoa))

// Object.assign (ECMAScript 2015)
const dest = {a: 1}
const o1 = {b: 3}
const o2 = { c: 3, d: 4}
const obj = Object.assign(dest, o1, o2)