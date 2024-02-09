// Retira algum elemento de um objeto { } ou de um array []. ES2015.

const pessoa = {
    nome: 'Ana',
    idade: 5, 
    endereco: {
        logradouro: 'Rua ABC',
        numero: 321
    }
}

const { nome, idade } = pessoa // {objeto1, objeto2} Operador de desestruturação.
// = objeto
console.log(nome, idade)

const { nome: n, idade: i } = pessoa
console.log(n, i)

const { sobrenome, bemHumorada = true } = pessoa
console.log(sobrenome, bemHumorada)

const {endereco: { logradouro, numero, cep}} = pessoa
console.log( logradouro, numero, cep)

const { conta: {ag,num}} = pessoa // Deve ter noçao do caminho "setado".