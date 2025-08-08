// Objeto: pode apresentar outros tipos de formatos como binário, executáveis, links, etc...

const obj = {a: 1, b: 2, c: 3, soma() {return a + b + c}}

// JSON: é um formato unicamente textual, todas as linguagens conseguem ler e gerar. 

// Transformando um Objeto para um JSON
// console.log(JSON.stringify(obj))

// Transformando um JSON para um Objeto
console.log(JSON.parse(obj))
console.log(JSON.parse('{ "a": 1.4, "b": "texto qualquer", "c": true, "d": {}, "e": [] }'))
