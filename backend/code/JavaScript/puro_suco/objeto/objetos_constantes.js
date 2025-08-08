// pessoa --> 123 --> {...}
const pessoa = {nome: 'Joao'}
pessoa.nome = 'Pedro'
console.log(pessoa)

// pessoa --> 323 --> {...}
// pessoa = { nome: 'Ana'}

Object.freeze(pessoa) // Congela o objeto

pessoa.nome = 'Maria'
console.log(pessoa.nome)

const pessoaConstante = Object.freeze({ nome: 'Jorge'})
pessoaConstante.nome = 'Maria'
console.log(pessoaConstante)